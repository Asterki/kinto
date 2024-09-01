import sys
import os
import unittest
from unittest.mock import patch

import dotenv

dotenv.load_dotenv()

# Add the directory containing the src module to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from src.index import App  # Use absolute import


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_showHelpMessage(self):
        with patch("builtins.print") as mock_print:
            self.app.showHelpMessage()
            mock_print.assert_called_with(
                "  log - Shows the latest 10 commits of the current branch\n   Usage: log\n"
            )

    def test_run_with_no_arguments(self):
        with patch("builtins.print") as mock_print:
            self.app.run()
            mock_print.assert_called_with("Type 'help' to see a list of commands")

    def test_run_with_invalid_command(self):
        with patch("builtins.print") as mock_print:
            self.app.run()
            mock_print.assert_called_with("Type 'help' to see a list of commands")

    def test_run_with_valid_command(self):
        sys.argv = ["kinto", "version"]

        with patch("builtins.print") as mock_print:
            self.app.run()
            mock_print.assert_called_with(
                "By: Asterki (https://github.com/Asterki"
            )


if __name__ == "__main__":
    unittest.main()
