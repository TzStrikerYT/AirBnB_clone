#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def  __init__():
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__():
        """Return a string of all atributtes of a instace"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    #Public instance methods
    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime.
        """
        self.update_at = datetime.now()

    def to_dict(self):
       """
       returns a dictionary containing all keys/values of
       __dict__ of the instance
       """
       
