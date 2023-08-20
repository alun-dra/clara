import webbrowser

from data.websites import websites

# Función para abrir sitios web basados en comandos de voz
def open_website(command):
    for site, url in websites.items():
        if site in command:
            webbrowser.open(url)
            return f"Abriendo {site} en tu navegador."

    return "Lo siento, no pude entender el comando para abrir un sitio web."