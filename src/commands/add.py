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
            commit = f.read().strip().split("\n")[0]

        # Get the current staging area
        with open(f".kinto/commits/{branch}/{commit}", "r") as f:
            current_staging_area = f.read().strip().split("\n")[1:]

        # Get the old staging area (if there is one)
        old_staging_area = []
        with open(f".kinto/branches/{branch}", "r") as f:
            doc = f.read().strip().split("\n")
            if (
                len(doc) >= 3
            ):  # If there's more than one commit, skip the first line since it's the current commit
                old_commit = doc[-2].split(" ")[0]
                
                print(old_commit)

                with open(f".kinto/commits/{branch}/{old_commit}", "r") as f:
                    old_staging_area = f.read().strip().split("\n")[1:]

        # Remove the U M D from the file names
        old_staging_area = list(map(lambda x: x[2:], old_staging_area))
        current_staging_area = list(map(lambda x: x[2:], current_staging_area))

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

                        if file not in current_staging_area:
                            current_staging_area.append(f"{file}")

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

                    if filePath not in current_staging_area:
                        current_staging_area.append(filePath)

        final_staging_area = []

        # Compare the current staging area with the old one
        if current_staging_area == old_staging_area:
            print("No changes detected, nothing to add")
            return
        else:
            for file in current_staging_area[1:]:
                if file not in old_staging_area:
                    # Add a U at the start of the file name
                    final_staging_area.append(f"U {file}")
                elif file in old_staging_area and file in current_staging_area:
                    # Add a M at the start of the file name
                    final_staging_area.append(f"M {file}")
            for file in old_staging_area:
                if file not in current_staging_area:
                    # Add a D at the start of the file name
                    final_staging_area.append(f"D {file}")

        # Write the new staging area
        with open(f".kinto/commits/{branch}/{commit}", "r+") as f:
            commit = f.read().strip().split("\n")[0]

            final_staging_area = "\n".join(final_staging_area)
            final_staging_area = final_staging_area.strip()

            f.seek(0)
            f.write(f"{commit}\n{final_staging_area}")

        print("File(s) added to the staging area")
