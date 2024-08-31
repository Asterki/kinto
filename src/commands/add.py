import os

import commands.command_base as command_base


class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Add a file to the staging area",
            "usage": "add filename.txt / add .",
            "aliases": []   
        }
        
    def run(self, *args):
        if len(args[0]) == 0:
            print("No file specified")
            return
        if args[0][0] == ".":
            files = os.listdir(os.getcwd())
            for file in files:
                if file.endswith(".txt"):
                    with open(file, "r") as f:
                        print(f.read())
        else:
            for file in args[0]:
                if not os.path.exists(file):
                    print(f"File '{file}' not found")
                else:
                    with open(file, "r") as f:
                        print(f.read())
        pass

    
