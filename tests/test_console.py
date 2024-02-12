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

"""
File exists

Test quit is present

console_0.py create_fake_console.py
msg -
Test EOF is present

console_1.py create_fake_console.py
msg -
Test help is present

console_2.py create_fake_console.py
Test “empty line” is present

console_3.py create_fake_console.py
msg -
Test create BaseModel is present

console_0.py
msg -
Test show BaseModel is present

console_1.py
Test destroy BaseModel is present

console_2.py
msg -
Test all BaseModel is present

console_3.py
msg -
Test update BaseModel is present

console_4.py
msg -
Test BaseModel.all() is present

console_0.py
msg -
Test Review.all() is present

console_6.py
msg -
Test User.all() is present

console_1.py
msg -
Test State.all() is present

console_2.py
msg -
Test City.all() is present

console_3.py
msg -
Test Amenity.all() is present

console_5.py
msg -
Test Place.all() is present

console_4.py
msg -
Test BaseModel.count() is present

console_0.py
msg -
Test User.count() is present

console_1.py
msg -
Test 1State.count()` is present

console_2.py
msg -
Test Place.count() is present

console_4.py
msg -
Test City.count() is present

console_3.py
msg -
Test Amenity.count() is present

console_5.py
msg -
Test Review.count() is present

console_6.py
msg -
Test BaseModel.show("id") is present

console_0.py
msg -
Test User.show("id") is present

console_1.py
msg -
Test State.show("id") is present

console_2.py
msg -
Test City.show("id") is present

console_3.py
msg -
Test Amenity.show("id") is present

console_5.py
msg -
Test Place.show("id") is present

console_4.py
msg -
Test Review.show("id") is present

console_6.py
msg -
Test BaseModel.destroy("id") is present

console_0.py
msg -
Test User.destroy("id") is present

console_1.py
msg -
Test City.destroy("id") is present

console_3.py
msg -
Test State.destroy("id") is present

console_2.py
msg -
Test Place.destroy("id") is present

console_4.py
msg -
Test Amenity.destroy("id") is present

console_5.py
msg -
Test Review.destroy("id") is present

console_6.py
msg -
Test BaseModel.update("id", "attribute_name", "string_value") is present

console_0.py
msg -
Test User.update("id", "attribute_name", "string_value") is present

console_1.py
msg -
Test State.update("id", "attribute_name", "string_value") is present

console_2.py
msg -
Test City.update("id", "attribute_name", "string_value") is present

console_3.py
msg -
Test Place.update("id", "attribute_name", "string_value") is present

console_4.py
msg -
Test Amenity.update("id", "attribute_name", "string_value") is present

console_5.py
msg -
Test Review.update("id", "attribute_name", "string_value") is present

console_6.py
msg -
Test BaseModel.update("id", { "attribute_name": "string_value" }) is present

console_0.py
msg -
Test User.update("id", { "attribute_name": "string_value" }) is present

console_1.py
msg -
Test State.update("id", { "attribute_name": "string_value" }) is present

console_2.py
msg -
Test Amenity.update("id", { "attribute_name": "string_value" }) is present

console_5.py
msg -
Test City.update("id", { "attribute_name": "string_value" }) is present

console_3.py
msg -
Test Place.update("id", { "attribute_name": "string_value" }) is present

console_4.py
msg -
Test Review.update("id", { "attribute_name": "string_value" }) is present

console_6.py
msg -
"""
