# app/main.py

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/message")
async def read_root():
    return {"hello": "world"}