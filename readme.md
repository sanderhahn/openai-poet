# OpenAI Poem Generator

Frontend: https://versify.fly.dev/
Backend: https://versify.fly.dev/docs

The application was created after a hackathon about using AI where we where challenged to create an application by (mostly) just talking to ChatGPT. For me it was quite a revelation what kind of help you get from the AI, but sometimes it is difficult to have it understand your exact requirements. Also it took more time than anticipated, but it gives you something to do in the weekend :) The images are generated based upon the texts that where generated using DreamStudio by Stability.ai with an Anime style.

Chat: https://chat.openai.com/share/2e23f875-6362-4fa6-bd48-5d47d4a2abf0
Source: https://github.com/sanderhahn/openai-poet

Development:

```sh
brew install python@3.11
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt.lock
uvicorn main:app --reload
```

The development was started, but not finished at the AI Hackathon at [Team-Rockstars-IT](https://github.com/Team-Rockstars-IT/Hackathon-AI).
