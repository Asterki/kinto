import sys
import dotenv
import os
import json
import shutil
import abc

dotenv.load_dotenv()


class App:
    def __init__(self) -> None:
        # Register the CLI commands
        commands = os.listdir(os.path.join(os.path.dirname(__file__), "commands"))
        commands = map(lambda x: x.replace(".py", ""), commands)
        
        print(list(commands))

    def showHelpMessage(self):
        print("Usage: python index.py [options]")
        print("Options:")
        print("  -h, --help    Show help message")
        print("  -v, --version Show version")

    def showVersion(self):
        version = os.environ.get("VERSION")
        print(f"Kinto v{version}")
        print("A simple command line version control system, written in Python")
        print("By: Asterki (https://github.com/Asterki)")

    def run(self):
        if len(sys.argv) == 1:
            self.showHelpMessage()
        elif len(sys.argv) == 2:
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                self.showHelpMessage()
            elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
                self.showVersion()
            else:
                print("Invalid option, see 'python index.py --help'")
        else:
            print("Invalid option")


if __name__ == "__main__":
    App().run()
