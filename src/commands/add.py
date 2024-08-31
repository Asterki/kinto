import os

import commands.command_base as command_base


# Add command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Add a file to the staging area",
            "usage": "add filename.txt / add .",
            "aliases": [],
        }

    def run(self, *args):
        if len(args[0]) == 0:
            print("No file specified")
            return

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

        # Get the ignored files inside .kintoignore
        ignored_files_or_folders = []
        if os.path.exists(".kintoignore"):
            with open(".kintoignore", "r") as f:
                ignored_files_or_folders = f.read().strip().split("\n")

        # Add the files to the staging area
        def add_files_in_folder(folder_path):
            files_in_folder = os.listdir(folder_path)
            files_with_full_path = [
                os.path.join(folder_path, file) for file in files_in_folder
            ]

            for file in files_with_full_path:
                if os.path.isdir(file) and file not in ignored_files_or_folders:
                    add_files_in_folder(file)
                else:
                    if file not in ignored_files_or_folders:
                        if not file.startswith("./"):
                            file = f"./{file}"

                        print(file)

                        # Check if the file is already in the staging area
                        if file not in staging_area:
                            staging_area.append(file)
                    else:
                        print(f"File/Folder '{file}' is ignored, it will not be added")

        for filePath in args[0]:
            # Check if the file is a folder
            if os.path.isdir(filePath):
                add_files_in_folder(filePath)
            else:
                # Check if the file exists and is not ignored
                if filePath not in ignored_files_or_folders and os.path.exists(
                    filePath
                ):
                    # Check if the file is already in the staging area
                    if not filePath.startswith("./"):
                        filePath = f"./{filePath}"

                    if filePath not in staging_area:
                        staging_area.append(filePath)
                else:
                    print(f"File '{filePath}' is ignored, it will not be added")

        # Write the new staging area
        with open(f".kinto/commits/{branch}/{commit}", "w") as f:
            staging_area = "\n".join(staging_area)
            staging_area = staging_area.strip()
            f.write(staging_area)

        print("====================================")
        print("File(s) added to the staging area")
