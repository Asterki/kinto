import sys
import dotenv
import os

dotenv.load_dotenv()


class App:
    def __init__(self) -> None:
        # Register the CLI commands
        self.command_list = os.listdir(
            os.path.join(os.path.dirname(__file__), "commands")
        )
        for i, command in enumerate(self.command_list):
            if not command.endswith(".py"):
                del self.command_list[i]
            else:
                self.command_list[i] = command.replace(".py", "")

        # Remove "command_base" from the list of commands
        self.command_list.remove("command_base")

        # Import the commands
        self.commands = {
            command: __import__(f"commands.{command}", fromlist=[command])
            for command in self.command_list
        }

        # Convert the commands to a list
        self.command_list = list(self.command_list)

        # Register the aliases
        self.new_commands = {}
        for command in self.commands:
            for alias in self.commands[command].Command().info["aliases"]:
                self.new_commands[alias] = self.commands[command]
                self.command_list.append(alias)
        self.commands.update(self.new_commands)

    def showHelpMessage(self):
        self.commands["help"].Command().run([])

    def run(self):
        if len(sys.argv) == 1:
            self.showHelpMessage()
        elif sys.argv[1] not in self.command_list:
            print(f"Command '{sys.argv[1]}' not found")
            print("Type 'help' to see a list of commands")
        else:
            # Run the command and pass any arguments the user may have given via the CLI
            command = self.commands.get(sys.argv[1]).Command()
            command.run(sys.argv[2:])


if __name__ == "__main__":
    App().run()
