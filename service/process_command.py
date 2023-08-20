import openai
import speech_recognition as sr

from service.openai_response import get_openai_response
from service.open_website import open_website
from service.open_application import open_application

from data.websites import websites
from data.applications import applications

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Función para realizar acciones basadas en comandos de voz
def process_command(command):
    command = command.lower()

    responses = {
        "hola clara": "¡Hola! ¿En qué puedo ayudarte?",
        "Cómo estás": "Bien y tu?",
        "adiós clara": "¡Hasta luego! Que tengas un buen día.",
        "preguntar": "Por favor, dime tu pregunta."
    }

    if "preguntar" in command:
        with open("respuestas_clara.txt", "a") as file:
            file.write("Usuario: " + command + "\n")

        with sr.Microphone() as source:
            print("Escuchando...")
            audio = recognizer.listen(source)

        user_question = recognizer.recognize_google(audio, language="es-ES")
        print("Pregunta del usuario:", user_question)

        try:
            openai_response = get_openai_response(user_question)
            response = "Aquí tienes la respuesta: " + openai_response

            with open("respuestas_clara.txt", "a") as file:
                file.write("Clara: " + response + "\n")
                file.write("\n")  # Separador entre conversaciones
        except openai.error.RateLimitError:
            response = "Se ha excedido la cuota de consultas de OpenAI. Por favor, verifica tu plan y facturación."

    else:
        response = responses.get(command, "Lo siento, no entendí ese comando.")
        
        if any(site in command for site in websites):
            response = open_website(command)
        elif any(app in command for app in applications):
            response = open_application(command)

    return response