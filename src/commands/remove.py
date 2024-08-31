import os

import commands.command_base as command_base


# Remove command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Remove a file from the staging area",
            "usage": "remove filename.txt",
            "aliases": ["rm"],
        }

    def run(self, *args):
        if len(args[0]) == 0:
            print("No file specified")
            return

        # Get the current branch
        with open(".kinto/HEAD", "r") as f:
            branch = f.read().strip()

        # Get the current commit
        with open(f".kinto/{branch}", "r") as f:
            commit = f.read().strip()

        # Get the current staging area
        with open(f".kinto/commits/{commit}", "r") as f:
            staging_area = f.read().strip().split("\n")

        new_staging_area = []

        # Remove the files from the staging area
        for file_path in args[0]:
            if not file_path.startswith("./"):
                file_path = f"./{file_path}"
                
            # If the file is a folder, remove it recursively
            if os.path.isdir(file_path):
                for line in staging_area:
                    if not line.startswith(file_path):
                        new_staging_area.append(line)
            else:
                if file_path not in staging_area:
                    print(f"File '{file_path}' is not in the staging area")
                else: 
                    new_staging_area = [line for line in staging_area if line != file_path]

        # Write the new staging area
        with open(f".kinto/commits/{commit}", "w") as f:
            f.write("\n".join(new_staging_area))
            
        print("File(s) removed from the staging area")
            