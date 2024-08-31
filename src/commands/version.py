import os

import commands.command_base as command_base


class Command(command_base.Command):
    def run(self, **kwargs):
        version = os.environ.get("VERSION")
        print(f"Kinto v{version}")
        print("A simple command line version control system, written in Python")
        print("By: Asterki (https://github.com/Asterki")

    @property
    def description(self):
        return "Show the version of the CLI"

    @property
    def usage(self):
        return "version"
