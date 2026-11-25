import os
import sqlite3
from config import DATABASE, DATA_DIR

def crear_directorio():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def crear_base_datos():
    crear_directorio()
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    # Crear tabla de espacios
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS espacios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL UNIQUE,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                capacidad INTEGER NOT NULL, 
                ubicacion TEXT,
                estado TEXT NOT NULL
            )
        ''')

    conexion.commit()
    conexion.close()

def insertar_datos_prueba():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM espacios")
    cantidad = cursor.fetchone()[0]

    if cantidad == 0:
        espacios = [
            ('LAB-01', 'Laboriatorio de computo 1', 'Laboratorio', 30, 'Edificio A - Nivel 1', 'Disponible'),
            ('AUL-01', 'Aula 101', 'Aula', 25, 'Edificio C - Nivel 1', 'Disponible'),
            ('AUD-01', 'Auditorio Principal', 'Auditorio', 200, 'Edificio B - Nivel 1', 'Disponible')
        ]

        cursor.executemany('''
                INSERT INTO espacios (
                codigo, nombre, tipo, capacidad, ubicacion, estado)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', espacios)

        conexion.commit()
        print("Datos de prueba insertados correctamente.")

    else:
        print("La base de datos ya contiene espacios")

        conexion.close()

def main():
    crear_base_datos()
    insertar_datos_prueba()

    print()
    print("Base de datos creada correctamente.")
    print(f"Ubicación: {DATABASE}")

if __name__ == "__main__":
    main()