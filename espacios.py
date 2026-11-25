import sqlite3

from database import obtener_conexion


ESTADOS_VALIDOS = {
    "DISPONIBLE",
    "OCUPADO",
    "MANTENIMIENTO"
}


def convertir_a_diccionario(fila):
    """
    Convierte una fila SQLite en un diccionario de Python.
    """

    return {
        "id": fila["id"],
        "codigo": fila["codigo"],
        "nombre": fila["nombre"],
        "tipo": fila["tipo"],
        "capacidad": fila["capacidad"],
        "ubicacion": fila["ubicacion"],
        "estado": fila["estado"]
    }


def obtener_todos_los_espacios():
    """
    Recupera todos los espacios registrados.

    Retorna una lista de diccionarios.
    """

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            codigo,
            nombre,
            tipo,
            capacidad,
            ubicacion,
            estado
        FROM espacios
        ORDER BY codigo
    """)

    filas = cursor.fetchall()

    conexion.close()

    espacios = []

    for fila in filas:
        espacio = convertir_a_diccionario(fila)

        espacios.append(espacio)

    return espacios


def buscar_espacio_por_codigo(codigo):
    """
    Busca un espacio utilizando su código.
    """

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            codigo,
            nombre,
            tipo,
            capacidad,
            ubicacion,
            estado
        FROM espacios
        WHERE UPPER(codigo) = UPPER(?)
    """, (codigo,))

    fila = cursor.fetchone()

    conexion.close()

    if fila is None:
        return None

    return convertir_a_diccionario(fila)


def obtener_espacios_disponibles():
    """
    Obtiene únicamente espacios cuyo estado es DISPONIBLE.
    """

    espacios = obtener_todos_los_espacios()

    disponibles = []

    for espacio in espacios:

        if espacio["estado"] == "DISPONIBLE":
            disponibles.append(espacio)

    return disponibles


def obtener_tipos_de_espacio():
    """
    Ejemplo de utilización de conjuntos.

    Recupera todos los tipos diferentes de espacios.
    """

    espacios = obtener_todos_los_espacios()

    tipos = set()

    for espacio in espacios:

        tipos.add(espacio["tipo"])

    return tipos

# NUEVO CODIGO: insercion de un nuevo espacio 
# en la base de datos.
def registrar_espacio(codigo, nombre, tipo, capacidad, ubicacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try: 
        cursor.execute("""
            INSERT INTO espacios (codigo, nombre, tipo, capacidad, ubicacion, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            codigo, nombre, tipo, capacidad, ubicacion, "DISPONIBLE"
            ))
        conexion.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexion.close()

def actualizar_espacio(codigo, nombre, tipo, capacidad, ubicacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE espacios
        SET 
            nombre = ?, tipo = ?, capacidad = ?, ubicacion = ?
        WHERE UPPER(codigo) = UPPER(?)
    """, (nombre, tipo, capacidad, ubicacion, codigo))

    
    conexion.commit()
    actualizado = cursor.rowcount > 0
    conexion.close()

    return actualizado