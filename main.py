
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

iniciar_sesion()
