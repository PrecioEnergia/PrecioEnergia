'''
Created on Apr 8, 2014

@author: gonzmg
'''
from google.appengine.ext import ndb

class PrecioEnergia(ndb.Model):
    """Models an individual precioenergia entry with an author, content, and date."""
    precio_espana = ndb.FloatProperty()
    precio_portugal = ndb.FloatProperty()
    fecha_prediccion = ndb.DateTimeProperty()
    fecha = ndb.DateTimeProperty()
    
    