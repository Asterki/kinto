import os

import commands.command_base as command_base


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
        if os.path.exists(".kinto"):
            print("Kinto repository reinitialized")
            return
        
        # Create the .kintoignore file
        with open(".kintoignore", "w") as f:
            f.write(".kinto\n.kintoignore\n")

        # Create the .kinto directory
        os.makedirs(".kinto")

        # Create the HEAD file
        with open(".kinto/HEAD", "w") as f:
            f.write("branches/heads/master")

        # Create the default branch (master)
        os.makedirs(".kinto/branches/heads")
        with open(".kinto/branches/heads/master", "w") as f:
            f.write("1")

        # Create the first commit
        os.makedirs(".kinto/commits")
        with open(".kinto/commits/1", "w") as f:
            f.write("")

        # Create the staging area
        with open(".kinto/commits/1", "w") as f:
            f.write("")
            
        # Create the filestore directory
        os.makedirs(".kinto/filestore")
            

        print("Initialized empty Kinto repository in .kinto")
        pass
