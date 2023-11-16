__all__ = ['LLMResultB']

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from .report import Report
from .scm import GitDiff

import os 

class LLMResultB:
    """ The intent of this class is to help us form several Prompt examples using a single application
        which we have already migrated.  We are using this single application and picking a few 
        violations our analyzer finds and then will construct a few prompt examples to assess the
        quality of response from a LLM
    """
    def __init__(self):
        """ We expect to have 2 directories that represent the same example application
            path_original_source is the original state of the application
            path_solved_source is the solved state of the application (after it has been migrated)
        """
        self.path_original_source = None
        self.path_solved_source = None
        self.path_to_report = None
        self.report = None 


    def set_path_original_source(self, example_initial_git_path):
        self.path_original_source = example_initial_git_path
    
    def set_path_solved_source(self, example_solved_git_path):
        self.path_solved_source = example_solved_git_path

    def parse_report(self, path_to_report):
        self.report = Report(path_to_report).get_report()

    def get_prompt_template(self):
        with open("./templates/template_02.txt", 'r') as f:
            template = f.read()
        return PromptTemplate.from_template(template)
    
    def _extract_diff(self, text: str):
        try:
            _, after = text.split("```diff")
            return after.split("```")[0]
        except Exception as e:
            print(f"Error: {e}")
            return "Error: Unable to extract diff"   

    def create_prompt(self, description, incidents, template):
        # To form a prompt we need:
        template = self.get_prompt_template()
        print(f"{len(incidents)} incidents:  {description}\n")

    def _update_uri(self, uri):
        return uri.replace("file:///opt/input/source/", "")
     
    def _ensure_output_dir_exists(self, output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except OSError as error:
            print(f"Error creating directory {output_dir}: {error}")
            raise error

    def _write_output(self, filename, content):
        with open(filename, 'w') as f:
            # We want to start each run with a clean file
            f.truncate(0)
            f.write(content)

    def process(self, model_name="", limit_to_rulesets=None, limit_to_violations=None):
        if self.report is None:
            raise Exception("No report to process.  Please parse a report first")
        if self.path_original_source is None:
            raise Exception("No 'path_original_source'.  Please use set_path_original_source()")
        if self.path_solved_source is None:
            raise Exception("No 'path_solved_source'.  Please use set_path_solved_source()")

        # Create result directory 
        self._ensure_output_dir_exists("./resultsB")

        for ruleset_name in self.report.keys():
            if limit_to_rulesets is not None and ruleset_name not in limit_to_rulesets:
                print(f"Skipping {ruleset_name} as it is not in {limit_to_rulesets}")
                continue
            ruleset = self.report[ruleset_name]
            ruleset_name_display = ruleset_name.replace('/', '_')
            print(f"Processing {ruleset_name} {ruleset_name_display}")
            for count, key in enumerate(ruleset['violations']):
                if limit_to_violations is not None and key not in limit_to_violations:     
                    print(f"Skipping {key} as it is not in {limit_to_violations}")
                    continue
                

                ###############################################################
                # For each violation, we will form only 1 prompt
                # If we have 2 incidents, we will use second as a 'solved' example, looking at the 
                # other repo which has the solved code present
                # Otherwise we will just send the prompt with the first incident
                #
                # Note this only a POC so we are intentionally ignoring other incidents that
                # would need to be solved.
                ###############################################################
                items = ruleset['violations'][key]

                if len(items['incidents']) == 0:
                    # No incidents so skip this iteration
                    continue
                
                description = items['description']
                current_issue_original_code =  items['incidents'][0].get('codeSnip', None)    
                lineNumber = items['incidents'][0].get('lineNumber', None)
                current_issue_filename = self._update_uri(items['incidents'][0]['uri'])
                current_issue_message = items['incidents'][0].get('message', None)  

                solved_example_filename = ""
                solved_example_diff = "" 
                if len(items['incidents']) > 1:
                    example_lineNumber = items['incidents'][1].get('lineNumber', None)
                    solved_example_filename = self._update_uri(items['incidents'][1]['uri'])
                    try:
                        gd = GitDiff(self.path_solved_source)
                        commit_main = gd.get_commit_from_branch('main')
                        commit_quarkus = gd.get_commit_from_branch('quarkus-migration')
                        solved_example_diff = gd.get_patch_for_file(commit_main.hexsha, commit_quarkus.hexsha, solved_example_filename)
                        #example_original_code = GitDiff(self.path_original_source).get_file_contents(example_original_filename)
                    except Exception as e:
                        print(f"Error: {e}")
                        solved_example_diff = ""
                        
                prompt = self.get_prompt_template()
                template_args = {
                    "description": description,
                    "current_issue_filename": current_issue_filename,
                    "current_issue_message": current_issue_message,
                    "current_issue_original_code": current_issue_original_code,
                    "solved_example_filename": solved_example_filename,
                    "solved_example_diff": solved_example_diff,
                }
                formatted_prompt = prompt.format(**template_args)
                #self._write_output(f"./results/{ruleset_name_display}_{key}_{count}_template.txt", formatted_prompt)
             
                llm = ChatOpenAI(temperature=0.1, model_name=model_name)
                chain = LLMChain(llm=llm, prompt=prompt)
                result = chain.run(template_args)
                result_diff = self._extract_diff(result)
                
                # Create result directory 
                self._ensure_output_dir_exists(f"./resultsB/{model_name}")
                with open(f"./resultsB/{model_name}/{ruleset_name_display}_{key}_{count}_full_run.md", "w") as f:
                    f.truncate(0)
                    f.write(f"## Prompt:\n")
                    f.write(f"{formatted_prompt}\n")
                    f.write(f"\n\n## Result:\n")
                    f.write(f"{result}\n\n")

                with open(f"./resultsB/{model_name}/{ruleset_name_display}_{key}_{count}.diff", "w") as f:
                    f.truncate(0)
                    f.write(result_diff)

        print(f"Process complete")

