import sys


class App:
    def __init__(self) -> None:
        pass
    
    def showHelpMessage(self):
        print("Usage: python index.py [options]")
        print("Options:")
        print("  -h, --help    Show help message")
        print("  -v, --version Show version")
    
    def run(self):
        if len(sys.argv) == 1:
            self.showHelpMessage()
        elif len(sys.argv) == 2:
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                self.showHelpMessage()
            elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
                print("1.0.0")
            else:
                print("Invalid option")
        else:
            print("Invalid option")


if __name__ == "__main__":
    App().run()    