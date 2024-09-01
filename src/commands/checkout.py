import os
import shutil

import commands.command_base as command_base


# Checkout command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Switch between Kinto branches",
            "usage": "checkout - checkout 'branch_name'",
            "aliases": [],
        }

    def run(self, *args):
        if not os.path.exists(".kinto"):
            print("Not a Kinto repository, run 'kinto init' to initialize")
            return

        if len(args[0]) == 0: # Show all the branches
            current_branch = ""
            with open(".kinto/HEAD", "r") as f:
                current_branch = f.read().strip().split("\n")[0]
            
            print(f"On branch {current_branch}")
            print("Branches:")
            for branch in os.listdir(".kinto/branches"):
                if branch == current_branch:
                    print(f"* {branch}")
                else:
                    print(f"  {branch}")
                    
            return 

        branch = args[0][0]
        if os.path.exists(f".kinto/branches/{branch}"):
            # Update the HEAD file
            with open(".kinto/HEAD", "w") as f:
                f.write(branch)
                
            # Get the current commit
            with open(f".kinto/branches/{branch}", "r") as f:
                commit = f.read().strip().split("\n")[0]
                
            # Move the files from the filestore, overwrite the existing files
            shutil.copytree(f".kinto/filestore/{branch}/{commit}", ".", dirs_exist_ok=True)
                
            print(f"Switched to branch '{branch}'")
        else:
            print(f"Branch '{branch}' does not exist")
            return
            