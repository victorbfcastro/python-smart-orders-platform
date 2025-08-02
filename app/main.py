from fastapi import FastAPI
from interfaces.api.routes import router as api_router

app = FastAPI(title="Orders API - Smart Orders Platform")

app.include_router(api_router)
