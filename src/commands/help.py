import os

import commands.command_base as command_base


class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Shows the help message",
            "usage": "help [command]",
            "aliases": ["-h", "--help"],
        }

    def run(self, *args):
        # Get all of the commands in this directory
        command_list = os.listdir(os.path.join(os.path.dirname(__file__), "."))

        # Remove the command_base.py and the help.py files
        command_list.remove("command_base.py")

        # Remove the .py extension
        for i, command in enumerate(command_list):
            if not command.endswith(".py"):
                del command_list[i]
            else:
                command_list[i] = command.replace(".py", "")

        # Import the commands
        commands = {
            command: __import__(f"commands.{command}", fromlist=[command])
            for command in command_list
        }

        # Convert the commands to a list
        command_list = list(command_list)

        # Show the help message
        if len(args[0]) == 0:
            print(
                "Kinto - A simple command line version control system, written in Python"
            )
            print("By: Asterki (https://github.com/Asterki)")

            print("\nCommands:")
            for command in commands:
                print(
                    f"  {command} - {commands[command].Command().info['description']}\n   Usage: {commands[command].Command().info['usage']}\n"
                )
        else:
            for command in args[0]:
                if command in command_list:
                    print(
                        f"{command} - {commands[command].Command().info['description']}\n  Usage: {commands[command].Command().info['usage']}"
                    )
                else:
                    print(f"Command '{command}' not found")
                    print("Type 'help' to see a list of commands")

        pass
