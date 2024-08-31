import os

import commands.command_base as command_base


class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Show the version of Kinto",
            "usage": "version",
            "aliases": ["v", "--version"]   
        }
        
    def run(self, *args):
        version = os.environ.get("VERSION")
        print(f"Kinto v{version}")
        print("A simple command line version control system, written in Python")
        print("By: Asterki (https://github.com/Asterki")

    
