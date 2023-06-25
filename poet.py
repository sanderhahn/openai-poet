import os

import openai
from dotenv import load_dotenv

import personas

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class PoetException(Exception):
    pass

def generate_poem(
        persona_code: str,
        friend: str,
        occasion: str,
        memory: str,
        prompt_template: str
    ) -> str:

    selected_persona = personas.get_persona(persona_code)

    # Construct the prompt using the provided inputs
    prompt = prompt_template.format(
        friend=friend,
        occasion=occasion,
        memory=memory,
        persona_nickname=selected_persona["nickname"],
    )

    # Access persona parameters
    temperature = selected_persona["temperature"]
    top_p = selected_persona["top_p"]
    frequency_penalty = selected_persona["frequency_penalty"]
    presence_penalty = selected_persona["presence_penalty"]

    # Use the parameters in OpenAI API call
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            best_of=1,
        )
        poem = response.choices[0].text.strip()
        return poem

    except openai.error.AuthenticationError as e:
        raise PoetException("OpenAI Auth Failed") from e
