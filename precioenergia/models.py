'''
Created on Apr 8, 2014

@author: gonzmg
'''
from google.appengine.ext import db

class Greeting(db.Model):
    """Models an individual precioenergia entry with an author, content, and date."""
    author = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def get_key_from_name(cls, precioenergia_name=None):
        return db.Key.from_path('precioenergia', precioenergia_name or 'default_precioenergia')