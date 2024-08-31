import sys
import dotenv
import os

dotenv.load_dotenv()


class App:
    def __init__(self) -> None:
        # Register the CLI commands
        commands = os.listdir(os.path.join(os.path.dirname(__file__), "commands"))
        commands = map(lambda x: x.replace(".py", ""), commands)
        self.commands = {
            command: __import__(f"commands.{command}", fromlist=[command])
            for command in commands
        } 
        self.commandList = commands  # Keep a register of the commands

    def showHelpMessage(self):
        self.commands["help"].Command().run()

    def run(self):
        if len(sys.argv) == 1 or sys.argv[1] not in self.commandList:
            self.commands["help"].Command().run()
        elif len(sys.argv) == 2:
            # Run the command and pass any arguments the user may have given via the CLI
            command = self.commands[sys.argv[1]].Command()
            command.run(sys.argv[2:])


if __name__ == "__main__":
    App().run()
