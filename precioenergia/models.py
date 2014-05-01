'''
Created on Apr 8, 2014

@author: gonzmg
'''
from google.appengine.ext import db

class PrecioEnergia(db.Model):
    """Models an individual precioenergia entry with an author, content, and date."""
    precio_espana = db.FloatProperty()
    precio_portugal = db.FloatProperty()
    date = db.DateTimeProperty()
    
    @classmethod
    def get_key_from_name(cls, precioenergia_name=None):
        return db.Key.from_path('precioenergia', precioenergia_name or 'default_precioenergia')