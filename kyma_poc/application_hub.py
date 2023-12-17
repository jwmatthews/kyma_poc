__all__ = ['ApplicationHub', 'Application']

import os
import shutil
import yaml 
import pprint

from io import StringIO
from kyma_poc.report import Report
from kyma_poc.scm import GitDiff

class Application:
    def __init__(self, name, report, repo, 
                initial_branch, solved_branch):
        self.name = name
        self.report = report
        self.repo = repo
        self.initial_branch = initial_branch
        self.solved_branch = solved_branch
        
class ApplicationHub:
    def __init__(self):
        # applications, keyed on App Name        
        self.applications = {}

        # cached_violations: {
        #   ruleset_name: { 
        #       violation_name: set(app_name1, app_name2, ...)
        #   }
        # }
        self.cached_violations = {}
    
    def add_application(self, name, yaml, repo, 
                        initial_branch="main", 
                        solved_branch=None):
        """
        Add an analysis to consider
        """
        # Verify repo, initial_branch, and solved_branch if valid
        gd = GitDiff(repo)
        #print(f"Checking {repo} has branches:  {gd.get_branches()}  ")
        try:
            #print(f"Checking {initial_branch} in {repo}")
            gd.get_commit_from_branch(initial_branch)
        except:
            raise FileNotFoundError(f"Branch {initial_branch} not found in {repo}") 
        
        if solved_branch:
            try:
                #print(f"Checking {initial_branch} in {repo}")
                gd.get_commit_from_branch(solved_branch)
            except:
                raise FileNotFoundError(f"Branch {initial_branch} not found in {repo}")

        report = Report(yaml).get_report()
        a = Application(name, report, repo, initial_branch, solved_branch)
        self.applications[name] = a
        self._update_cached_violations(a)
    
    def get_application(self, name):
        return self.applications[name]
    
    def get_application_names(self):
        return self.applications.keys()
    
    def find_common_violation(self, ruleset_name, violation_name):
        """     
        Find the common violation across all applications
        Returns:
            None        - if no common violation
            [AppNames]  - if a common violaiton is found
        """
        if self.cached_issues is None:
            return None
        ruleset = self.cached_issues.get(ruleset_name, None)
        if ruleset is None:
            print(f"Unable to find cached_violations for ruleset: '{ruleset_name}'")
            return None
        return self.cached_issues[ruleset_name].get(violation_name, None)        
     

    def _update_cached_violations(self, a):
        """
        Update the cached_violations with the new application
        """
        ### Add our Application's Name to the cached_violations
        #pp = pprint.PrettyPrinter(indent=2)
        #pp.pprint(a.report)

        for ruleset in a.report.keys():
            if ruleset not in self.cached_violations:
                self.cached_violations[ruleset] = {}
            for violation_name in a.report[ruleset]['violations'].keys():
                if violation_name not in self.cached_violations[ruleset]:
                    self.cached_violations[ruleset][violation_name] = set()
                self.cached_violations[ruleset][violation_name].add(a.name)