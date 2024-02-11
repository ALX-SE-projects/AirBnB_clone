import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys

class TestConsole(unittest.TestCase):
    hbnb_command = HBNBCommand()

    @patch('sys.stdout', new=StringIO())
    def test_help_show(self):
        self.hbnb_command.onecmd("help show")
        output = sys.stdout.getvalue().strip()
        self.assertIn("Prints the string representation of an instance",
            output
            )

    @patch('sys.stdout', new=StringIO())
    def test_quit(self):
        pass

    test_EOF = test_quit

    @patch('sys.stdout', new=StringIO())
    def test_emptyline(self):
        pass

    @patch('sys.stdout', new=StringIO())
    def test_onecmd(self):
        # .all
        # .count()
        # .show
        # .destroy
        # .update
        pass



if __name__ == '__main__':
    unittest.main()
