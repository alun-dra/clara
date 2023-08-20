import openai
import os

# Función para obtener respuestas de OpenAI
def get_openai_response(prompt):
    
    # Configura tu clave de API de OpenAI
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("No se ha definido la clave de API de OpenAI en las variables de entorno.")
    
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=5000
    )
    return response.choices[0].text.strip()