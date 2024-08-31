import os
import shutil

import commands.command_base as command_base


# Branch command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Manage kinto branches",
            "usage": "branch - branch 'branch_name' - branch remove 'branch_name'",
            "aliases": [],
        }

    def run(self, *args):
        if not os.path.exists(".kinto"):
            print("Not a Kinto repository, run 'kinto init' to initialize")
            return

        if len(args[0]) == 0: # Show all the branches
            current_branch = ""
            with open(".kinto/HEAD", "r") as f:
                current_branch = f.read().strip()
            
            print(f"On branch {current_branch}")
            print("Branches:")
            for branch in os.listdir(".kinto/branches"):
                if branch == current_branch:
                    print(f"* {branch}")
                else:
                    print(f"  {branch}")
                    
            return 

        if args[0][0] == "remove":
            if len(args[0]) == 1:
                print("No branch specified")
                return

            # Avoid removing the master branch
            branch = args[0][1]
            if branch == "master":
                print("Cannot remove the master branch")
                return

            # Check if the branch exists
            if not os.path.exists(f".kinto/branches/{branch}"):
                print(f"Branch '{branch}' does not exist")
                return

            # Remove the branch
            os.remove(f".kinto/branches/{branch}")
            shutil.rmtree(f".kinto/commits/{branch}")
            shutil.rmtree(f".kinto/filestore/{branch}")
            

            print(f"Branch '{branch}' removed")
            return

        branch = args[0][0]
        if os.path.exists(f".kinto/branches/{branch}"):
            print(f"Branch '{branch}' already exists")
            return

        with open(f".kinto/branches/{branch}", "w") as f:
            f.write("1")

        os.makedirs(f".kinto/commits/{branch}")
        os.makedirs(f".kinto/filestore/{branch}/1")

        print(f"Branch '{branch}' created")
