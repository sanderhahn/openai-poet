from enum import Enum

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import personas
import poet

# FastAPI app
app = FastAPI()

class PersonaEnum(str, Enum):
    ww = "ww"
    ee = "ee"
    ss = "ss"
    mm = "mm"
    ll = "ll"

# Request model
class PoemRequest(BaseModel):
    persona_code: PersonaEnum = PersonaEnum.ww
    friend: str = "Sander"
    occasion: str = "Christmas"
    memory: str = "OpenAI Hackathon"
    prompt_template: str = """
        Write a poem for your friend {friend} on the occasion of {occasion}.
        Reflect upon a pleasurable memory when {memory} happend that you both
        experienced.
        Make the poem at least 10 lines long and ensure each line ends with proper
        punctuation.
        Don't abruptly end the poem and ensure end rhyme in the verse.
    """

    class Config:
        schema_extra = {
            "example": {
                "friend": "John",
                "occasion": "Birthday",
                "memory": "Our trip to the beach",
                "persona_code": "ww"  # Example persona code
            }
        }

@app.exception_handler(personas.PersonaException)
async def persona_exception_handler(request, exc):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

# @app.exception_handler(poet.PoetException)
# async def poet_exception_handler(request, exc):
#     return JSONResponse(status_code=500, content={"detail": str(exc)})

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={
        "error": str(exc),
        "class": exc.__class__.__name__,
    })

# Endpoint to generate a poem
@app.post("/generate_poem")
async def generate_poem(poem_request: PoemRequest):
    poem = poet.generate_poem(
        persona_code=poem_request.persona_code,
        friend=poem_request.friend,
        occasion=poem_request.occasion,
        memory=poem_request.memory,
        prompt_template=poem_request.prompt_template,
    )
    return {"poem": poem}

# Create a Jinja2Templates instance pointing to the "templates" directory
templates = Jinja2Templates(directory="templates")

# Endpoint to serve the HTML form
@app.get("/", include_in_schema=False)
async def form(request: Request):
    return templates.TemplateResponse("poem_form.html", {
        "personas": personas.personas,
        "request": request,
    })

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/test", include_in_schema=False)
async def test(request: Request):
    return templates.TemplateResponse("test.html", {
        "request": request,
    })

@app.get("/health", include_in_schema=False)
def read_root():
    return {"status": "ok"}
