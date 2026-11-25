import sqlite3
from config import DATABASE

def obtener_conexion():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion



