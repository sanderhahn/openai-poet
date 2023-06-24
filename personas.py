# Persona definitions
personas = [
    {
        "code": "WW",
        "nickname": "Whispering Willow",
        "temperature": 0.5,
        "top_p": 0.8,
        "frequency_penalty": 0.2,
        "presence_penalty": 0.5
    },
    {
        "code": "EE",
        "nickname": "Enigmatic Echo",
        "temperature": 0.7,
        "top_p": 0.9,
        "frequency_penalty": 0.4,
        "presence_penalty": 0.2
    },
    {
        "code": "SS",
        "nickname": "Serenade Star",
        "temperature": 0.6,
        "top_p": 0.7,
        "frequency_penalty": 0.1,
        "presence_penalty": 0.6
    },
    {
        "code": "MM",
        "nickname": "Mystic Muse",
        "temperature": 0.8,
        "top_p": 0.5,
        "frequency_penalty": 0.3,
        "presence_penalty": 0.3
    },
    {
        "code": "LL",
        "nickname": "Lyrical Luna",
        "temperature": 0.4,
        "top_p": 0.6,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.7
    }
]

def get_persona(persona_code):
    return next(
        persona
        for persona in personas
        if persona["code"] == persona_code
    )

def get_persona_codes():
    return [persona["code"] for persona in personas]

def generate_personas_dict():
    personas_dict = {persona['code']: persona['nickname'] for persona in personas}
    return personas_dict
