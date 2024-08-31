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
            print("Kinto repository already exists")
            return
        os.makedirs(".kinto")
        os.makedirs(".kinto/branches")
        os.makedirs(".kinto/commits")
        with open(".kinto/HEAD", "w") as f:
            f.write("refs/heads/master")
        print("Initialized empty Kinto repository in .kinto")
        pass
