import os

from data.applications import applications

# Función para abrir aplicaciones basadas en comandos de voz
def open_application(command):
    for app, command_name in applications.items():
        if app in command:
            os.system(command_name)
            return f"Abriendo {app}."

    return "Lo siento, no pude entender el comando para abrir una aplicación."

