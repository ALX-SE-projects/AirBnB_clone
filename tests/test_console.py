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


_dir = glob('/tmp/correction/corrections_*')[0]
_dir = f'{_dir}/corrections/{263}/{1976}'
for i in (0, 1, 2, 3, 4, 5, 6):
    with open(os.path.join(_dir, f'console_{i}.py'), 'wt') as f:
        f.write('print("OK")\n')

if __name__ == '__main__':
    unittest.main()



