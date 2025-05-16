from fastapi import FastAPI
from interface.api.routes import router as prompt_router
from interface.api.write_routes import router as write_router

app = FastAPI(
    title="AI Proxy Agent API",
    description="REST API to interact with your AI-powered dev assistant",
    version="1.0.0"
)

app.include_router(prompt_router)
app.include_router(write_router)
