#!/usr/bin/python3
"module containing BaseModel class"

from datetime import datetime
from uuid import uuid4
from . import storage
import os
print(os.listdir('/files/correction_system/'))
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