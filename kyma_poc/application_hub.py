__all__ = ['ApplicationHub', 'Application']

import os
import shutil
import yaml 

from io import StringIO
from kyma_poc.report import Report
from kyma_poc.scm import GitDiff

class Application:
    def __init__(self, name, yaml, repo, 
                initial_branch, solved_branch, report=None):
        self.name = name
        self.yaml = yaml
        self.repo = repo
        self.initial_branch = initial_branch
        self.solved_branch = solved_branch
        self.report = report

class ApplicationHub:
    def __init__(self):
        # applications, keyed on App Name        
        self.applications = {}

        # issues, keyed on issue ID
        self.cached_issues = {}
    
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

        r = Report(yaml).get_report()
        a = Application(name, yaml, repo, initial_branch, solved_branch, r)
        self.applications[name] = a
    
    def get_application(self, name):
        return self.applications[name]
    
    def get_application_names(self):
        return self.applications.keys()
    
    def process_issues(self):
        """
        Process all applications
        """
        # Drop prior cached_issues
        self.cached_issues = None

        for app_name, app in self.applications.values():
            report = app.report
            # Process Report and get ALL issues
            # Build a cached_issues as:
            # key = ISSUE ID
            # value = [App Name]

            # Assume will need another lookup of Issue, App Name = Impacted Files

            #app = self.process_application(app_name)

