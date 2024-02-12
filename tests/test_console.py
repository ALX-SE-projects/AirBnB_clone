import unittest
from unittest.mock import patch
from io import StringIO
import sys
from glob import glob
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__) + '/..'))
HBNBCommand = __import__('console').HBNBCommand


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
        ...

    test_EOF = test_quit

    @patch('sys.stdout', new=StringIO())
    def test_emptyline(self):
        ...

    @patch('sys.stdout', new=StringIO())
    def test_onecmd(self):
        # .all
        # .count()
        # .show
        # .destroy
        # .update
        ...

    @patch('sys.stdout', new=StringIO())
    def test_all(self):
        # .all
        # .count()
        # .show
        # .destroy
        # .update
        ...

    @patch('sys.stdout', new=StringIO())
    def test_show(self):
        # .all
        # .count()
        # .show
        # .destroy
        # .update
        ...

if __name__ == '__main__':
    unittest.main()
