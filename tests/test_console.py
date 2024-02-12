import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys


class TestConsole(unittest.TestCase):
    @patch('sys.stdout', new=StringIO())
    def test_help_show(self):
        hbnb_command = HBNBCommand()
        hbnb_command.onecmd("help show")
        output = sys.stdout.getvalue().strip()
        self.assertIn(
            "Prints the string representation of an instance",
            output
            )

    @patch('sys.stdout', new=StringIO())
    def test_quit(self):
        return True

    test_EOF = test_quit

    @patch('sys.stdout', new=StringIO())
    def test_emptyline(self):
        return True

    @patch('sys.stdout', new=StringIO())
    def test_onecmd(self):
        # .all
        # .count()
        # .show
        # .destroy
        # .update
        return True

    @patch('sys.stdout', new=StringIO())
    def test_all(self):
        # .all
        # .count()
        # .show
        # .destroy
        # .update
        return True

    @patch('sys.stdout', new=StringIO())
    def test_show(self):
        # .all
        # .count()
        # .show
        # .destroy
        # .update
        return True


if __name__ == '__main__':
    unittest.main()
