import os

import commands.command_base as command_base


class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Shows the help message",
            "usage": "help [command]",
            "aliases": ["-h", "--help"]   
        }
        
    def run(self, *args):
        self.commands = os.environ.get("VERSION")
        pass

