import os

import commands.command_base as command_base

# Constants
KINTO_DIR = ".kinto"
KINTO_IGNORE = f"{KINTO_DIR}ignore"
HEAD_FILE = f"{KINTO_DIR}/HEAD"
BRANCHES_DIR = f"{KINTO_DIR}/branches"
COMMITS_DIR = f"{KINTO_DIR}/commits"
FILESTORE_DIR = f"{KINTO_DIR}/filestore"
DEFAULT_BRANCH = "main"

# Init command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Initialize a new Kinto repository",
            "usage": "init",
            "aliases": [],
        }

    def run(self, *args):
        if os.path.exists(KINTO_DIR):
            print("Kinto repository reinitialized in existing directory.")
            return

        try:
            # Create the .kintoignore file
            with open(KINTO_IGNORE, "w") as f:
                f.write(f"./{KINTO_DIR}\n./{KINTO_IGNORE}\n")

            # Create the .kinto directory structure
            os.makedirs(KINTO_DIR)
            os.makedirs(BRANCHES_DIR)
            os.makedirs(f"{COMMITS_DIR}/{DEFAULT_BRANCH}")
            os.makedirs(f"{FILESTORE_DIR}/{DEFAULT_BRANCH}/1")

            # Create the HEAD file and set to default branch
            with open(HEAD_FILE, "w") as f:
                f.write(DEFAULT_BRANCH)

            # Create the first commit in the default branch
            with open(f"{COMMITS_DIR}/{DEFAULT_BRANCH}/1", "w") as f:
                f.write("Initial commit")

            # Record the initial commit in the branch log
            with open(f"{BRANCHES_DIR}/{DEFAULT_BRANCH}", "w") as f:
                f.write("1")

            print(f"Initialized empty Kinto repository in {KINTO_DIR}")

        except Exception as e:
            print(f"Failed to initialize repository: {e}")
