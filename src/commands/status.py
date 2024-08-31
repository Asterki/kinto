import os

import commands.command_base as command_base


# Status command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Show current staging area status",
            "usage": "status",
            "aliases": ["st"],
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

        if len(staging_area) == 0:
            print("No files in the staging area")
        else:
            print(f"On branch {branch}, commit {commit}, staging area:")
            if len(staging_area) == 1 and staging_area[0] == "":
                print("  No files in the staging area")
            elif len(staging_area) > 10:
                for file in staging_area[:10]:
                    print(f"  {file}")
                print(f"  ... and {len(staging_area) - 10} more")

        pass
