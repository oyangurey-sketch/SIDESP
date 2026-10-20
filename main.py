
# ==========================================
# SIDESP - MESA DE PARTES DIGITAL (UPN)
# VERSIÓN 1: ESTRUCTURA INICIAL
# ==========================================

# Lista de trabajadores autorizados
lista_trabajadores = [
    {
        "id": "A001",
        "pase": "1234",
        "cargo": "Administrador",
        "nombre": "Marcelo Bendezú"
    },
    {
        "id": "A002",
        "pase": "5678",
        "cargo": "Asistente",
        "nombre": "Ana Sulca"
    }
]

# Lista para almacenar los expedientes
lista_expedientes = []

# Nombre del archivo para guardar los datos
ARCHIVO_DATOS = "expedientes.txt"
# ==========================================
# MÓDULO 3: PERSISTENCIA DE DATOS
# ==========================================

import json
import os


# Función para guardar los expedientes
def guardar_expedientes():
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(lista_expedientes, archivo, ensure_ascii=False, indent=4)
    except OSError:
        print("Error: no se pudieron guardar los expedientes.")


# Función para cargar los expedientes
def cargar_expedientes():
    global lista_expedientes

    if not os.path.exists(ARCHIVO_DATOS):
        lista_expedientes = []
        return

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            lista_expedientes = json.load(archivo)

        if not isinstance(lista_expedientes, list):
            lista_expedientes = []
            print("Advertencia: el archivo no contiene una lista válida.")

    except (OSError, json.JSONDecodeError):
        lista_expedientes = []
        print("Advertencia: no se pudieron cargar los expedientes.")

# ==========================================
# MÓDULO 1: AUTENTICACIÓN
# ==========================================

# Función para validar las credenciales
def validar_credenciales(ID, contraseña):
    for trabajador in lista_trabajadores:
        if trabajador["id"] == ID and trabajador["pase"] == contraseña:
            return trabajador
    return None

# Función para iniciar sesión
def iniciar_sesion():
    print("\n========== INICIO DE SESIÓN ==========")
    ID = input("Ingrese su ID de trabajador: ")
    contraseña = input("Ingrese su contraseña: ")
    trabajador = validar_credenciales(ID, contraseña)
    if trabajador is not None:
        print(f"\nBienvenido(a), {trabajador['nombre']}")
        print(f"Cargo: {trabajador['cargo']}")
        gestionar_roles(trabajador)
        return trabajador
    else:
        print("\nError: ID o contraseña incorrectos.")
        return None

# Mensaje inicial del sistema
print("========================================")
print(" SIDESP - MESA DE PARTES DIGITAL (UPN)")
print("========================================")
print("Estructura inicial cargada correctamente.")

# ==========================================
# EJECUCIÓN DEL INICIO DE SESIÓN
# ==========================================
# ==========================================
# MÓDULO 4: GESTIÓN DE EXPEDIENTES
# ==========================================

# Función para registrar expedientes
def registrar_expediente():
    print("\n========== REGISTRO DE EXPEDIENTE ==========")

    codigo = f"EXP-{len(lista_expedientes) + 1:03d}"

    fecha = input("Ingrese fecha de registro (DD/MM/AAAA): ").strip()
    if not fecha:
        fecha = "19/10/2026"

    nombre = input("Ingrese nombre completo del ciudadano: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese nombre completo del ciudadano: ").strip()

    print("\nSeleccione tipo de documento:")
    print("1. DNI")
    print("2. Pasaporte")
    print("3. Carnet de extranjería")

    opcion_doc = input("Seleccione una opción (1-3): ").strip()

    while opcion_doc not in ("1", "2", "3"):
        print("Opción inválida.")
        opcion_doc = input("Seleccione una opción (1-3): ").strip()

    if opcion_doc == "1":
        tipo_documento = "DNI"
        documento = input("Ingrese DNI (8 dígitos): ").strip()

        while len(documento) != 8 or not documento.isdigit():
            print("El DNI debe contener exactamente 8 dígitos.")
            documento = input("Ingrese DNI (8 dígitos): ").strip()

    elif opcion_doc == "2":
        tipo_documento = "Pasaporte"
        documento = input("Ingrese número de pasaporte: ").strip()

        while not documento:
            print("El número de pasaporte no puede estar vacío.")
            documento = input("Ingrese número de pasaporte: ").strip()

    else:
        tipo_documento = "Carnet de extranjería"
        documento = input("Ingrese número de carnet: ").strip()

        while not documento:
            print("El número de carnet no puede estar vacío.")
            documento = input("Ingrese número de carnet: ").strip()

    asunto = input("Ingrese asunto del expediente: ").strip()
    while not asunto:
        print("El asunto no puede estar vacío.")
        asunto = input("Ingrese asunto del expediente: ").strip()

    area = input("Ingrese área de destino: ").strip()
    while not area:
        print("El área no puede estar vacía.")
        area = input("Ingrese área de destino: ").strip()

    expediente = {
        "codigo": codigo,
        "fecha": fecha,
        "nombre": nombre,
        "tipo_documento": tipo_documento,
        "documento": documento,
        "asunto": asunto,
        "area": area,
        "estado": "Registrado"
    }

    lista_expedientes.append(expediente)
    guardar_expedientes()

    print("\nExpediente registrado correctamente.")
    print("Código asignado:", codigo)
# Función para consultar expedientes
def consultar_expediente():
    print("\n========== CONSULTA DE EXPEDIENTES ==========")

    if not lista_expedientes:
        print("No hay expedientes registrados en el sistema.")
        return

    criterio = input(
        "Ingrese el código del expediente o número de documento: "
    ).strip()

    encontrado = None

    for expediente in lista_expedientes:
        if (
            expediente["codigo"] == criterio
            or expediente["documento"] == criterio
        ):
            encontrado = expediente
            break

    if encontrado is None:
        print("Expediente no encontrado.")
        return

    print("\n========== DETALLE DEL EXPEDIENTE ==========")
    print("Código             :", encontrado["codigo"])
    print("Fecha              :", encontrado["fecha"])
    print("Ciudadano          :", encontrado["nombre"])
    print("Tipo de documento  :", encontrado["tipo_documento"])
    print("Número de documento:", encontrado["documento"])
    print("Asunto             :", encontrado["asunto"])
    print("Área de destino    :", encontrado["area"])
    print("Estado             :", encontrado["estado"])
# Función para modificar expedientes
def modificar_expediente():
    print("\n========== MODIFICACIÓN DE EXPEDIENTE ==========")

    if not lista_expedientes:
        print("No hay expedientes registrados.")
        return

    codigo = input("Ingrese el código del expediente: ").strip()

    expediente_encontrado = None

    for expediente in lista_expedientes:
        if expediente["codigo"] == codigo:
            expediente_encontrado = expediente
            break

    if expediente_encontrado is None:
        print("Expediente no encontrado.")
        return

    print("\n¿Qué desea modificar?")
    print("1. Nombre del ciudadano")
    print("2. Número de documento")
    print("3. Asunto")
    print("4. Área de destino")
    print("5. Estado")

    opcion = input("Seleccione una opción (1-5): ").strip()

    if opcion == "1":
        nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()

        if nuevo_nombre:
            expediente_encontrado["nombre"] = nuevo_nombre
        else:
            print("El nombre no puede estar vacío.")
            return

    elif opcion == "2":
        nuevo_documento = input("Ingrese el nuevo número de documento: ").strip()

        if expediente_encontrado["tipo_documento"] == "DNI":
            if len(nuevo_documento) != 8 or not nuevo_documento.isdigit():
                print("El DNI debe contener exactamente 8 dígitos.")
                return

        elif not nuevo_documento:
            print("El documento no puede estar vacío.")
            return

        expediente_encontrado["documento"] = nuevo_documento

    elif opcion == "3":
        nuevo_asunto = input("Ingrese el nuevo asunto: ").strip()

        if nuevo_asunto:
            expediente_encontrado["asunto"] = nuevo_asunto
        else:
            print("El asunto no puede estar vacío.")
            return

    elif opcion == "4":
        nueva_area = input("Ingrese la nueva área de destino: ").strip()

        if nueva_area:
            expediente_encontrado["area"] = nueva_area
        else:
            print("El área no puede estar vacía.")
            return

    elif opcion == "5":
        print("1. Registrado")
        print("2. En proceso")
        print("3. Atendido")

        nuevo_estado = input("Seleccione el nuevo estado (1-3): ").strip()

        estados = {
            "1": "Registrado",
            "2": "En proceso",
            "3": "Atendido"
        }

        if nuevo_estado not in estados:
            print("Opción inválida.")
            return

        expediente_encontrado["estado"] = estados[nuevo_estado]

    else:
        print("Opción inválida.")
        return

    guardar_expedientes()
    print("Expediente modificado correctamente.")
# Función para ordenar y listar expedientes
def ordenar_expedientes():
    print("\n========== LISTADO DE EXPEDIENTES ==========")

    if not lista_expedientes:
        print("No hay expedientes registrados.")
        return

    lista_ordenada = sorted(
        lista_expedientes,
        key=lambda expediente: expediente["codigo"]
    )

    print("-" * 115)
    print(
        f"{'CÓDIGO':<12}"
        f"{'FECHA':<14}"
        f"{'CIUDADANO':<25}"
        f"{'DOCUMENTO':<22}"
        f"{'ESTADO':<16}"
    )
    print("-" * 115)

    for expediente in lista_ordenada:
        documento_completo = (
            expediente["tipo_documento"]
            + ": "
            + expediente["documento"]
        )

        print(
            f"{expediente['codigo']:<12}"
            f"{expediente['fecha']:<14}"
            f"{expediente['nombre'][:24]:<25}"
            f"{documento_completo[:21]:<22}"
            f"{expediente['estado']:<16}"
        )

    print("-" * 115)
    print("Total de expedientes:", len(lista_ordenada))
# ==========================================
# MÓDULO 2: GESTIÓN DE ROLES Y PERMISOS
# ==========================================

# Función para mostrar y procesar el menú del Administrador
def menu_administrador():
    while True:
        print("\n========== MENÚ ADMINISTRADOR ==========")
        print("1. Registrar expediente")
        print("2. Consultar expedientes")
        print("3. Modificar expediente")
        print("4. Ordenar expedientes")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("La función de registro se implementará próximamente.")
        elif opcion == "2":
            print("La función de consulta se implementará próximamente.")
        elif opcion == "3":
            print("La función de modificación se implementará próximamente.")
        elif opcion == "4":
            print("La función de ordenamiento se implementará próximamente.")
        elif opcion == "5":
            print("\nSesión cerrada.")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")


# Función para mostrar y procesar el menú del Asistente
def menu_asistente():
    while True:
        print("\n========== MENÚ ASISTENTE ==========")
        print("1. Registrar expediente")
        print("2. Consultar expedientes")
        print("3. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("La función de registro se implementará próximamente.")
        elif opcion == "2":
            print("La función de consulta se implementará próximamente.")
        elif opcion == "3":
            print("\nSesión cerrada.")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")
# Función para gestionar los roles
def gestionar_roles(trabajador):
    cargo = trabajador["cargo"]

    if cargo == "Administrador":
        print("\nAcceso autorizado: Administrador")
        menu_administrador()  
    elif cargo == "Asistente":
        print("\nAcceso autorizado: Asistente")
        menu_asistente()    
    else:
        print("\nError: Cargo no reconocido.")

iniciar_sesion()
