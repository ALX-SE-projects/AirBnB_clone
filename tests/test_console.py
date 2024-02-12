import unittest
from unittest.mock import patch
from io import StringIO
import sys
from glob import glob
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__) + '/..'))
HBNBCommand = __import__('console').HBNBCommand
hbnb_command = HBNBCommand()

@patch('sys.stdout', new=StringIO())
def tst(line):
    hrbnb_command.onecmd(line)
    sys.stdout.getvalue().strip()


class TestConsole(unittest.TestCase):

    def test_help_show(self):
        tst("help show")
        tst("help")
        tst("")
        tst("create")
        tst("show")
        tst("destroy")
        tst("all")
        tst("update")
        tst("City.count()")
        tst("Place.count()")
        tst("State.count()")
        tst("User.count()")
        tst("BaseModel.count()")
        # tst("")
        # tst("")
        # tst("")
        # tst("")
        # tst("")
        # tst("")
        # tst("")
        # tst("")
        # tst("")
        tst("quit")
        tst("EOF")


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
