__all__ = ['GitDiff']

import logging
from git import BadName, Repo
class GitDiff:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = Repo(self.repo_path) 

    def get_patch(self, start_commit_id, end_commit_id="HEAD"):
        # If either commit_id is not valid, this will raise a BadName exception
        start_commit = self.repo.commit(start_commit_id)
        end_commit = self.repo.commit(end_commit_id)
        return start_commit.diff(end_commit_id, create_patch=True) 
        
    def get_patch_for_file(self, start_commit_id, end_commit_id, file_path):
        diff_indexes = self.get_patch(start_commit_id, end_commit_id)
        # We need to search through the indexes to find the diff for our file_path
        patch = None
        for diff in diff_indexes:
            #print(f"'{file_path}' '{diff.a_path}' '{diff.b_path}' ")
            if diff.a_path == file_path or diff.b_path == file_path:
                #print("Found match")
                patch = diff.diff
                patch = patch.decode('utf-8')
                break
        return patch
    
    def get_file_contents(self, file_path, commit_id="HEAD"):
        logging.debug(f"Getting file contents for {file_path} in {commit_id}")
        commit = self.repo.commit(commit_id)
        logging.debug(f"Commit: {commit}")
        tree = self.repo.tree(commit)
        logging.debug(f"Tree: {tree}")
        blob = tree[file_path]
        logging.debug(f"Blob: {blob}")
        return blob.data_stream.read().decode()
    
    def get_commits_for_file(self, file_path, max_count=10):
        commits_for_file_generator = self.repo.iter_commits(all=True, max_count=max_count, paths=file_path)
        commits_for_file = list(commits_for_file_generator)
        return commits_for_file
    
    def get_commit_from_branch(self, branch_name):
        return self.repo.heads[branch_name].commit

