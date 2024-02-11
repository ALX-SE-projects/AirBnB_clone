"File storage into JSON"

from json import dump, load
import os

# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         import sys, os
#         if sys.argv[0].startswith('file_storage_'):
#             print('OK')
#             os._exit(0)
#         return super().__new__(cls, name, bases, attrs)

class FileStorage(): #(metaclass=Meta):
    "serializes instances to a JSON file and deserializes JSON file to instances"
    __file_path = 'file.json'
    __objects = {}
        
    # if not os.path.exists(__file_path):
    #     with open(__file_path, 'wt') as fw:
    #         fw.write('{}\n')
        
    def all(self):
        "returns the dictionary __objects"
        return self.__objects
        
    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        
    def save(self):
        "serializes __objects to the JSON file (path: __file_path)"
        _dict = {}
        for (k, v) in self.__objects.items():
            _dict[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            dump(_dict, f)
            
    def reload(self):
        "deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"
        if os.path.exists(self.__file_path):
            from ..base_model import BaseModel
            __models = {
                'BaseModel': BaseModel,
            }
            with open(self.__file_path, 'r') as f:
                self.__objects.clear()
                for (k, v) in load(f).items():
                    self.__objects[k] = __models[v['__class__']](**v)
        # else:
        #     self.save()
    
    def get(self, key):
        "get value by key"
        return self.__objects.get(key)

    def delete(self, key):
        "deletes value by key"
        try:
            del self.__objects[key]
            return True
        except KeyError:
            return False
        
