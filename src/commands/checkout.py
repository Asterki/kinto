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

        if len(args[0]) == 0:  # Show all the branches
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

        # Check if there are staged files
        with open(".kinto/HEAD", "r") as f:
            current_branch = f.read().strip().split("\n")[0]

        with open(f".kinto/branches/{current_branch}", "r") as f:
            current_commit = f.read().strip().split("\n")[0]

        if os.path.exists(f".kinto/commits/{current_branch}/{current_commit}"):
            with open(f".kinto/commits/{current_branch}/{current_commit}", "r") as f:
                staging_area = f.read().strip().split("\n")[1:]

            if len(staging_area) > 0:
                return print(
                    "You have staged files, please commit them before switching branches"
                )
                

        branch = args[0][0]
        if os.path.exists(f".kinto/branches/{branch}"):
            # Update the HEAD file
            with open(".kinto/HEAD", "w") as f:
                f.write(branch)

            # Get the current commit
            with open(f".kinto/branches/{branch}", "r") as f:
                commit = f.read().strip().split("\n")[0]
                
            if branch == current_branch:
                print(f"Already on branch '{branch}'")
                return
                
            if commit == "1":
                print("You can't switch to another branch without first committing")
                return
                
            # Move the files from the filestore, overwrite the existing files
            shutil.copytree(
                f".kinto/filestore/{branch}/{commit}", ".", dirs_exist_ok=True
            )
            
            # Remove the files that are not in the new branch
            # TODO

            print(f"Switched to branch '{branch}'")
        else:
            print(f"Branch '{branch}' does not exist")
            return
