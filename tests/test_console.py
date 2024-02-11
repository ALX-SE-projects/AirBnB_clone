import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys

class TestConsole(unittest.TestCase):

    @patch('sys.stdout', new=StringIO())
    def test_help_show(self):
        # Instantiate the command object
        hbnb_command = HBNBCommand()

        # Execute the help show command
        hbnb_command.onecmd("help show")

        # Capture the output
        output = sys.stdout.getvalue().strip()

        # Assert that the output is as expected
        self.assertIn("Prints the string representation of an instance",
            output
            )

    # Add more test methods for other commands and scenarios

if __name__ == '__main__':
    unittest.main()
