from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import personas
import poet

# FastAPI app
app = FastAPI()

# Request model
class PoemRequest(BaseModel):
    persona_code: str = "WW"
    recipient_name: str = "Sander"
    occasion: str = "Christmas"
    memory: str = "OpenAI Hackathon"
    prompt_template: str = """
        Prompt: Write a poem for {recipient_name} on the occasion of {occasion}.
        Reflect upon a pleasurable memory when {memory} happend that you both
        experienced.
        Make the poem at least 10 lines long and ensure each line ends with proper
        punctuation.
        Don't abruptly end the poem and make sure it ends with a nice rhyme.
    """

    class Config:
        schema_extra = {
            "example": {
                "recipient_name": "John",
                "occasion": "Birthday",
                "memory": "Our trip to the beach",
                "persona_code": "WW"  # Example persona code
            }
        }

# Endpoint to generate a poem
@app.post("/generate_poem")
async def generate_poem(poem_request: PoemRequest):
    poem = poet.generate_poem(
        persona_code=poem_request.persona_code,
        recipient_name=poem_request.recipient_name,
        occasion=poem_request.occasion,
        memory=poem_request.memory,
        prompt_template=poem_request.prompt_template,
    )
    return {"poem": poem}

# Create a Jinja2Templates instance pointing to the "templates" directory
templates = Jinja2Templates(directory="templates")

# Endpoint to serve the HTML form
@app.get("/")
async def form(request: Request):
    return templates.TemplateResponse("poem_form.html", {
        "personas": personas.generate_personas_dict(),
        "request": request,
    })

app.mount("/static", StaticFiles(directory="static"), name="static")
