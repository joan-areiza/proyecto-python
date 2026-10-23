# SQLTools
"""
Proyecto Python y MySQL por consola
- Abrir un asistente
- Login o registro
- Si elegimos registro, creara un usuario en la BD
- Si elegimos login, identifica al usuario y nos pregunta
- Crear nota, mostrar notas, borrarlas
"""

from usuarios import acciones

print("""
Acciones disponibles:
- registro
- login
""")

hazel = acciones.Acciones()

accion = input("¿Que quiere hacer?: ")

if accion == "registro":
    hazel.registro()

elif accion == "login":
    hazel.login()




