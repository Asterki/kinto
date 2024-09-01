import random
import os
import shutil
from datetime import datetime

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
            commit = f.read().strip().split("\n")[0]

        # Get the current staging area
        with open(f".kinto/commits/{branch}/{commit}", "r") as f:
            staging_area = f.read().strip().split("\n")[1:]

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

        if len(staging_area) == 1:
            print("No files in the staging area")
            answer = input("Do you want to commit an empty commit? (y/n): ")
            if answer.lower() != "y":
                return

        # Create the folder structure
        for file in staging_area:
            if file.count("/") > 1:  # This means that the file is inside a folder
                folder_path = file[4:]  # Remove the "./" from the file path, including U M D (staging area)
                folder_path = "/".join(
                    folder_path.split("/")[:-1]
                )  # Remove the file name from the path

                if not os.path.exists(
                    f".kinto/filestore/{branch}/{commit}/{folder_path}"
                ):
                    os.makedirs(f".kinto/filestore/{branch}/{commit}/{folder_path}")

        # Copy the files to the filestore
        for file in staging_area:
            if not file.startswith("D "):  # If the file is not deleted
                shutil.copy(file[4:], f".kinto/filestore/{branch}/{commit}/{file[4:]}")

        # Write the new commit
        with open(f".kinto/commits/{branch}/{commit}", "w") as f:
            f.write(f"{commit_message}\n")  # Add the commit message

        # Update the branch
        with open(f".kinto/branches/{branch}", "r+") as f:
            current_content = f.read().strip().split("\n")
            # Change the current commit to the new commit (the first line)
            current_content[0] = commit

            # Update the history
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_content.append(f"{commit} - {date}: {commit_message}")

            # Write the updated content back to the file
            f.seek(0)
            f.write("\n".join(current_content))
            f.truncate()
            

        print(commit_message)
        print("====================================")
        print("\n".join(staging_area))
        print("====================================")
        print("Changes committed")
        print(f"Commit hash: {commit}")
