import os

from config import TITULO_SISTEMA, ANCHO_PANTALLA

from espacios import (
    obtener_todos_los_espacios,
    buscar_espacio_por_codigo,
    obtener_espacios_disponibles,
    obtener_tipos_de_espacio,
    registrar_espacio,
    actualizar_espacio
)


def limpiar_pantalla():
    """
    Limpia la terminal dependiendo del sistema operativo.
    """

    os.system("cls" if os.name == "nt" else "clear")


def linea(caracter="="):
    """
    Imprime una línea utilizando el ancho definido.
    """

    print(caracter * ANCHO_PANTALLA)


def titulo(texto):
    """
    Muestra encabezados centrados.
    """

    linea("=")

    print(texto.center(ANCHO_PANTALLA))

    linea("=")


def pausa():

    print()

    input("Presione ENTER para continuar...")


def menu_principal():

    limpiar_pantalla()

    titulo(TITULO_SISTEMA)

    print()
    print("  1. Listar espacios")
    print("  2. Consultar espacio")
    print("  3. Ver espacios disponibles")
    print("  4. Ver tipos de espacios")
    print("  5. Registrar espacio")
    print("  6. Actualizar espacio")
    print("  7. Salir")
    print()

    linea("-")

    opcion = input("Seleccione una opción: ")

    return opcion


def mostrar_tabla(espacios):

    if not espacios:

        print()
        print("No existen registros para mostrar.")

        return

    print()

    print(
        f"{'CÓDIGO':<10}"
        f"{'NOMBRE':<30}"
        f"{'TIPO':<16}"
        f"{'CAP.':<7}"
        f"{'ESTADO':<15}"
    )

    linea("-")

    for espacio in espacios:

        print(
            f"{espacio['codigo']:<10}"
            f"{espacio['nombre'][:28]:<30}"
            f"{espacio['tipo'][:14]:<16}"
            f"{espacio['capacidad']:<7}"
            f"{espacio['estado']:<15}"
        )


def listar_espacios():

    limpiar_pantalla()

    titulo("LISTADO GENERAL DE ESPACIOS")

    espacios = obtener_todos_los_espacios()

    mostrar_tabla(espacios)

    print()

    linea("-")

    print(f"Total de espacios registrados: {len(espacios)}")

    pausa()


def consultar_espacio():

    limpiar_pantalla()

    titulo("CONSULTA DE ESPACIO")

    print()

    codigo = input(
        "Ingrese el código del espacio: "
    ).strip()

    if codigo == "":

        print()
        print("Debe ingresar un código.")

        pausa()

        return

    espacio = buscar_espacio_por_codigo(codigo)

    if espacio is None:

        print()
        print("Espacio no encontrado.")

        pausa()

        return

    print()

    linea("-")

    print(f"Código       : {espacio['codigo']}")
    print(f"Nombre       : {espacio['nombre']}")
    print(f"Tipo         : {espacio['tipo']}")
    print(f"Capacidad    : {espacio['capacidad']} personas")
    print(f"Ubicación    : {espacio['ubicacion']}")
    print(f"Estado       : {espacio['estado']}")

    linea("-")

    pausa()

##### NUEVA FUNCION #####
def registrar_nuevo_espacio():
    limpiar_pantalla()
    titulo("REGISTRO DE ESPACIO")

    codigo = input("Código:  ").strip()
    nombre = input("Nombre:  ").strip()
    tipo = input("Tipo:  ").strip()
    capacidad_texto = input("Capacidad:  ").strip()
    ubicacion = input("Ubicación (opcional):  ").strip()

    if codigo == "" or nombre == "" or tipo == "":
        print("Codigo, nombre y tipo son obligatorios.")
        pausa()
        return

    try:
        capacidad = int(capacidad_texto)
    except ValueError:
        print("\nLa capacidad debe ser un número entero.")
        pausa()
        return

    if capacidad <= 0:
        print("\nLa capacidad debe ser mayor a cero.")
        pausa()
        return

    if buscar_espacio_por_codigo(codigo) is not None:
        print("\nYa existe un espacio con ese código.")
        pausa()
        return

    registrado = registrar_espacio(
        codigo, nombre, tipo, capacidad, ubicacion
        )

    if registrado:
        print("\nEspacio registrado correctamente.")
    else:
        print("\nNo se pudo registrar el espacio.")

    pausa()
##### FIN NUEVA FUNCION #####

##### NUEVA FUNCION 3 #####
def actualizar_datos_espacio():
    limpiar_pantalla()
    titulo("ACTUALIZACIÓN DE ESPACIO")
    print()

    codigo = input("Código del espacio a actualizar: ").strip()

    if codigo == "":
        print()
        print("Debe ingresar un código.")
        pausa()
        return

    espacio = buscar_espacio_por_codigo(codigo)

    if espacio is None:
        print()
        print("Espacio no encontrado.")
        pausa()
        return

    print()
    print("Presione ENTER para mantener el valor actual.")
    print()

    nombre = input(f"Nombre [{espacio['nombre']}]: ").strip()

    tipo = input(f"Tipo [{espacio['tipo']}]: ").strip()
    
    capacidad_texto = input(f"Capacidad [{espacio['capacidad']}]: ").strip()

    ubicacion_actual = espacio['ubicacion'] or "" 
    ubicacion = input(f"Ubicación [{ubicacion_actual}]: ").strip()

    if nombre == "":
        nombre = espacio['nombre']

    if tipo == "":
        tipo = espacio['tipo']

    if capacidad_texto == "":
        capacidad = espacio['capacidad']
    else:
        try:
            capacidad = int(capacidad_texto)
        except ValueError:
            print()
            print("La capacidad debe ser un número entero.")
            pausa()
            return

    if capacidad <= 0:
        print()
        print("La capacidad debe ser mayor a cero.")
        pausa()
        return

    if ubicacion == "":
        ubicacion = ubicacion_actual

    actualizado = actualizar_espacio(
        espacio["codigo"], nombre, tipo, capacidad, ubicacion
    )

    print()

    if actualizado:
        print("Espacio actualizado correctamente.")
    else:
        print("No se pudo actualizar el espacio.")

    pausa()

##### FIN NUEVA FUNCION #####


def listar_disponibles():

    limpiar_pantalla()

    titulo("ESPACIOS DISPONIBLES")

    espacios = obtener_espacios_disponibles()

    mostrar_tabla(espacios)

    print()

    linea("-")

    print(
        f"Cantidad de espacios disponibles: "
        f"{len(espacios)}"
    )

    pausa()


def listar_tipos():

    limpiar_pantalla()

    titulo("TIPOS DE ESPACIOS")

    tipos = obtener_tipos_de_espacio()

    print()

    if not tipos:

        print("No existen tipos registrados.")

    else:

        tipos_ordenados = sorted(tipos)

        contador = 1

        for tipo in tipos_ordenados:

            print(f"  {contador}. {tipo}")

            contador += 1

    print()

    linea("-")

    print(f"Cantidad de tipos diferentes: {len(tipos)}")

    pausa()


def ejecutar_sistema():

    while True:

        opcion = menu_principal()

        if opcion == "1":

            listar_espacios()

        elif opcion == "2":

            consultar_espacio()

        elif opcion == "3":

            listar_disponibles()

        elif opcion == "4":

            listar_tipos()

        ####
        elif opcion == "5":

            registrar_nuevo_espacio()
        ###

        ###
        elif opcion == "6":

            actualizar_datos_espacio()
        ###


        elif opcion == "7":

            limpiar_pantalla()

            titulo(TITULO_SISTEMA)

            print()
            print(
                "Sistema finalizado correctamente."
                .center(ANCHO_PANTALLA)
            )
            print()

            break

        else:

            print()
            print("Opción incorrecta.")

            pausa()


if __name__ == "__main__":

    ejecutar_sistema()