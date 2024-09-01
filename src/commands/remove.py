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
        with open(f".kinto/branches/{branch}", "r") as f:
            commit = (
                f.read().strip().split("\n")[0]
            )  # I'm not removing the first line (commit message) since it would be a hassle to re-add it

        # Get the current staging area
        with open(f".kinto/commits/{branch}/{commit}", "r") as f:
            staging_area = f.read().strip().split("\n")

        file_name = args[0][0]


        # Filter out the entries that end with the specified file_name
        new_staging_area = "\n".join(list(filter(lambda x: not x.split(" ")[1].endswith(file_name), staging_area)))

        # Write the new staging area
        with open(f".kinto/commits/{branch}/{commit}", "w") as f:
            f.write(new_staging_area)

        print("File(s) removed from the staging area")
