import random
import os
import shutil

import commands.command_base as command_base


# Commit command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Commits the changes in the staging area",
            "usage": "commit 'Your commit message'",
            "aliases": [],
        }

    def run(self, *args):
        if not os.path.exists(".kinto"):
            print("Not a Kinto repository, run 'kinto init' to initialize")
            return
        
        # Get the current branch
        with open(".kinto/HEAD", "r") as f:
            branch = f.read().strip()
            

        # Get the current commit
        with open(f".kinto/branches/{branch}", "r") as f:
            commit = f.read().strip()

        # Get the current staging area
        with open(f".kinto/commits/{branch}/{commit}", "r") as f:
            staging_area = f.read().strip().split("\n")

        # Get the commit message
        commit_message = " ".join(args[0])

        # Check if the commit message is empty
        if not commit_message:
            print("Please provide a commit message")
            return

        # Generate a random commit hash
        commit = "".join(random.choices("abcdef0123456789", k=10))

        # Create the new commit folder
        os.mkdir(f".kinto/filestore/{branch}/{commit}")

        # Create the folder structure
        for file in staging_area:
            if file.count("/") > 1:  # This means that the file is inside a folder
                folder_path = file[2:]  # Remove the "./" from the file path
                folder_path = "/".join(
                    folder_path.split("/")[:-1]
                )  # Remove the file name from the path

                if not os.path.exists(
                    f".kinto/filestore/{branch}/{commit}/{folder_path}"
                ):
                    os.makedirs(f".kinto/filestore/{branch}/{commit}/{folder_path}")

        # Copy the files to the filestore
        for file in staging_area:
            shutil.copy(file, f".kinto/filestore/{branch}/{commit}/{file[2:]}")
            
        # Write the new commit
        with open(f".kinto/commits/{branch}/{commit}", "w") as f:
            f.write("\n") # Empty commit
            
        # Update the branch
        with open(f".kinto/branches/{branch}", "w") as f:
            f.write(commit)

        print("\n".join(staging_area))
        print("====================================")
        print("Changes committed")
        print(f"Commit hash: {commit}")
