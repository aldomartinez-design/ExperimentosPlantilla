
from python.models.modelos import *
from sqlalchemy import String, Text, or_,func,Integer, Float, Numeric
from sqlalchemy.sql import case
from flask import session,flash
import re
import json
from datetime import date, datetime
from decimal import Decimal
from python.services.system.helper_functions import *
from python.services.system.email import *

#####
# funciones de formularios
#####

HANDLERS = {}

def handler_edit_on_success(*tables):
    def wrapper(fn):
        for t in tables:
            HANDLERS[t] = fn
        return fn
    return wrapper

def edit_on_success(table_name, id, changed_fields=None):
    handler = HANDLERS.get(table_name)
    if not handler:
        return
    return handler(id, changed_fields)
'''
@handler_edit_on_success('ejemplo')
def ejemplo(id, changed_fields):

'''

@handler_edit_on_success('ordenes_de_compra')
def ordenes_de_compra(id, changed_fields):
    compra=OrdenesDeCompra.query.get(id)
    if compra.notas is not None:
        compra.estatus='Finalizada'
