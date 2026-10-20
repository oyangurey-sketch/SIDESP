
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