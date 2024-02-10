"File storage into JSON"

from json import dump, load
import os

class FileStorage:
    "serializes instances to a JSON file and deserializes JSON file to instances"
    
    def __init__(self, *args, **kwargs):
        if 'file_path' in kwargs.keys():
            self.__file_path = kwargs['file_path']
        else:
            self.__file_path = 'file.json'
        self.__objects = {}
        
    def all(self):
        "returns the dictionary __objects"
        return self.__objects
        
    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        self.__objects[f"{obj['__class__']}.{obj['id']}"] = obj
        
    def save(self):
        "serializes __objects to the JSON file (path: __file_path)"
        with open(self.__file_path, 'w') as f:
            dump(self.__objects, f)
            
    def reload(self):
        "deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = load(f)
            