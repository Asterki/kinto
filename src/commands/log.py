import os

import commands.command_base as command_base


# Log command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Shows the latest 10 commits of the current branch",
            "usage": "log",
            "aliases": []
        }
        
    def run(self, *args):
        if not os.path.exists(".kinto"):
            print("Not a Kinto repository, run 'kinto init' to initialize")
            return
        
        # Get the current branch
        with open(".kinto/HEAD", "r") as f:
            branch = f.read().strip()
            
        # Get the current commits 
        with open(f".kinto/branches/{branch}", "r") as f:
            commits = f.read().strip().split("\n")[1:]
            
        print(f"On branch {branch}")
        print("Commits:")
        for commit in commits[-10:]:
            print(f"  {commit}")
        

    
