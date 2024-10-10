# commands/config.py

import commands.command_base as command_base
from config_controller import ConfigController

class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Get or set repository or global options.",
            "usage": "config --get <section.option> | config --set <section.option> <value> [--global]",
            "aliases": [],
        }

    def run(self, *args):
        # Basic argument parsing
        if len(args) < 2:
            print("Invalid usage. See usage: config --get <section.option> | --set <section.option> <value> [--global]")
            return

        # Determine if this is a global config operation
        global_flag = "--global" in args
        args = [arg for arg in args if arg != "--global"]

        # Initialize the config controller
        config = ConfigController(global_config=global_flag)

        # Parse the arguments for get/set
        command = args[0]
        section, option = args[1].split(".")

        if command == "--get":
            value = config.get(section, option)
            if value is None:
                print(f"Config value {section}.{option} not found.")
            else:
                print(f"{section}.{option}={value}")

        elif command == "--set" and len(args) == 3:
            config.set(section, option, args[2])
            print(f"Set {section}.{option} to {args[2]} in {'global' if global_flag else 'local'} config.")

        else:
            print("Invalid arguments. Use --get <section.option> or --set <section.option> <value> [--global]")
