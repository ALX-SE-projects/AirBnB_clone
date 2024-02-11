#!/usr/bin/python3
"""dev console module"""

import cmd

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
        
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()