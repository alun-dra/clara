import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import speech_recognition as sr

class GUI:
    def __init__(self, process_command):
        self.process_command = process_command
        self.recognizer = sr.Recognizer()

        self.app = tk.Tk()
        self.app.title("Asistente Virtual")

        self.command_label = tk.Label(self.app, text="Di algo:")
        self.command_label.pack()

        self.command_entry = scrolledtext.ScrolledText(self.app, width=40, height=4)
        self.command_entry.pack()

        self.response_label = tk.Label(self.app, text="Respuesta:")
        self.response_label.pack()

        self.response_text = scrolledtext.ScrolledText(self.app, width=40, height=4, state=tk.DISABLED)
        self.response_text.pack()

    def listen_for_command(self):
        thread = Thread(target=self.listen_and_process)
        thread.start()

    def listen_and_process(self):
        microphone = sr.Microphone()
        while True:
            with microphone as source:
                print("Escuchando...")
                audio = self.recognizer.listen(source)

            print("Procesando...")
            command = self.recognizer.recognize_google(audio, language="es-ES")
            print("Comando detectado:", command)

            response = self.process_command(command)
            print("Respuesta:", response)

            self.update_response_text(response)

    def update_response_text(self, response):
        self.response_text.config(state=tk.NORMAL)
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response)
        self.response_text.config(state=tk.DISABLED)

    def process_voice_command(self):
        command = self.command_entry.get("1.0", tk.END).strip()
        response = self.process_command(command)
        self.update_response_text(response)

    def run(self):
        self.listen_and_process()  # Inicia la escucha y el procesamiento automáticamente
        self.app.mainloop()


