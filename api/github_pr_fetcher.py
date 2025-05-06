from github import Github
from typing import List, Dict

class GitHubPRFetcher:
    def __init__(self, token: str, repo_name: str):
        self.client = Github(token)
        self.repo = self.client.get_repo(repo_name)

    def get_pull_request(self, pr_number: int) -> Dict:
        pr = self.repo.get_pull(pr_number)
        files = pr.get_files()
        commits = pr.get_commits()

        return {
            "title": pr.title,
            "body": pr.body,
            "author": pr.user.login,
            "diffs": [
                {
                    "filename": f.filename,
                    "patch": f.patch,
                } for f in files if f.patch
            ],
            "commits": [
                {
                    "message": c.commit.message,
                    "author": c.commit.author.name
                } for c in commits
            ]
        }
