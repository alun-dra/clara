import speech_recognition as sr
from service.process_command import process_command

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()


# Ciclo principal del asistente
while True:
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = recognizer.listen(source)

        print("Procesando...")
        command = recognizer.recognize_google(audio, language="es-ES")
        print("Comando detectado:", command)

        response = process_command(command)
        print("Respuesta:", response)

    except sr.UnknownValueError:
        print("No se pudo entender el audio. Inténtalo de nuevo.")
    except sr.RequestError as e:
        print(f"Error en la solicitud a Google Speech Recognition: {e}")
