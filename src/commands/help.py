import os

import commands.command_base as command_base

class Command(command_base.Command):
    def run(self, **kwargs):
        self.commands = os.environ.get("VERSION")
        print(f"Kinto v{self.commands}")
        print("A simple command line version control system, written in Python")

    @property
    def description(self):
        return "Shows the help message"

    @property
    def usage(self):
        return "help [command]"
