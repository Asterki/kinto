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
            f.write("./.kinto\n./.kintoignore\n")

        # Create the .kinto directory
        os.makedirs(".kinto")

        # Create the HEAD file
        with open(".kinto/HEAD", "w") as f:
            f.write("master")

        # Create the default branch (master)
        os.makedirs(".kinto/branches")
        with open(".kinto/branches/master", "w") as f:
            f.write("1")

        # Create the first commit 
        os.makedirs(".kinto/commits/master")
        with open(".kinto/commits/master/1", "w") as f:
            f.write("Initial commit")
            
        # Create the filestore directory for the master branch
        os.makedirs(".kinto/filestore/master/1")
            
        print("Initialized empty Kinto repository in .kinto")
        pass
