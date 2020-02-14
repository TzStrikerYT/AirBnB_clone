#!/usr/bin/python3
"""MOdule for save and read since a file"""
import json
import os

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict of a object"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            res = {key: value.to_dict() for key,
                   value in FileStorage.__objects.items()}
            json.dump(res, f)

    def reload(self):
        """ Deserializes JSON file """
        from models.base_model import BaseModel

        if os.path.isfile(FileStorage.__file_path) is True:
            dict_class = {"BaseModel": BaseModel}

            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    self.new(dict_class[value["__class__"]](**value))