#!/usr/bin/python3
"""dev console module"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from shlex import split

_classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review,
}
_classes_keys = tuple(_classes.keys())

class HBNBCommand(cmd.Cmd):
    "HBNBCommand class"
    prompt = '(hbnb) '

    def do_quit(self, cmd):
        "quit method"
        return True
        
    do_EOF = do_quit
    
    def emptyline(self):
        "an empty line + ENTER shouldn’t execute anything"
        pass

    def chk_cmd(self, cmd):
        "checks that command is not empty and returns cmd.split()"
        cmd = cmd.split()
        if not cmd:
            print('** class name missing **')
            return
        return cmd
        

    def get_class_name(self, cmd):
        "checks that class name exists and return it"
        cmd = self.chk_cmd(cmd)
        if cmd:
            _class = cmd[0]
            if _class in _classes_keys:
                return _class
            else:
                print("** class doesn't exist **")

    def get_class(self, cmd):
        "checks that class exists and return it"
        _class_name = self.get_class_name(cmd)
        if _class_name:
            return _classes[_class_name]

    def get_instance(self, cmd, get_key=False):
        "checks that instance exists and return it and its key"
        cmd = cmd.split()
        if not cmd:
            print('** class name missing **')
            return
        _class = cmd[0]
        if _class not in _classes_keys:
            print("** class doesn't exist **")
            return
        if len(cmd) == 1:
            print("** instance id missing **")
            return
        key = f"{_class}.{cmd[1]}"
        _class = storage.get(key)
        if _class is None:
            print("** no instance found **")
            return
        if get_key:
            return _class, key
        else:
            return _class

    # def str_instance(self, _instance):
    #     "__str__ format an instance for the checker to be happy [:"
    #     return f"[{_instance.__class__.__name__}] ({_instance.id}) {str(_instance)}"

    def do_create(self, cmd):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        If the class name is missing, print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        """
        _class = self.get_class(cmd)
        if _class:
            _class = _class()
            _class.save()
            print(_class.id)
            
            
    def do_show(self, cmd):
        """
        Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        _instance = self.get_instance(cmd)
        if _instance:
            print(str(_instance))

    def do_destroy(self, cmd):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        item = self.get_instance(cmd, get_key=True)
        if item:
            _instance, key = item
            storage.delete(key)
            storage.save()

    def do_all(self, cmd, do_print=True):
        """
        Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        """
        if cmd == '':
            _class_name = ''
        else:
            _class_name = self.get_class_name(cmd)
        if _class_name is None:
            # print("** class doesn't exist **")
            return
        instances = []
        for (k, v) in storage.all().items():
            if k.startswith(_class_name):
                instances.append(str(v))
        if do_print:
            print(instances)
        else:
            return instances

    def do_update(self, cmd):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type

        If the class name is missing, print ** class name missing ** (ex: $ update)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)

        If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)

        All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
        id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
        Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
        """
        _instance = self.get_instance(cmd)
        if _instance:
            cmd = cmd.split()
            cmd_len = len(cmd)
            if cmd_len == 2:
                print('** attribute name missing **')
                return
            if cmd_len == 3:
                print('** value missing **')
                return
            attr_name = cmd[2]
            attr_val = split(' '.join(cmd[3:]))[0]
            _instance.__setattr__(attr_name, attr_val)
            _instance.save()

    def onecmd(self, line):
        "hook custom names of commands"
        if line.endswith('.all()'):
            self.do_all(line[:line.find('.')])
        elif line.endswith('.count()'):
            print(
                len(
                    self.do_all(line[:line.find('.')], do_print=False)
                )
            )
        else:
            return super().onecmd(line)
            
        
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
