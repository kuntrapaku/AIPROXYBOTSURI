# agent/agent_server.py

"""
This file runs a FastAPI server to expose the AI Agent via an HTTP API.
Java (Spring Boot) or any client can call this API.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.agent_core import ask_agent

app = FastAPI()

# ✅ Enable CORS so frontend/backend can call this easily
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow from all origins (you can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define request schema
class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
async def handle_ask(req: PromptRequest):
    """
    Handle incoming prompt from frontend/backend.
    Calls the agent and returns a response.
    """
    user_prompt = req.prompt
    reply = ask_agent(user_prompt)
    return {"response": reply}
