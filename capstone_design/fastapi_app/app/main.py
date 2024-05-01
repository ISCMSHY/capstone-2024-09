# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Request
from pydantic import BaseModel
from .open_ai import get_chat_response
from .db_query import save_chats, get_job_categories
from typing import List, Dict, Union
from fastapi.responses import UJSONResponse

app = FastAPI(default_response_class=UJSONResponse)

origins = [
    "http://localhost:3000",  # React 앱의 도메인
    "http://fastapi_app:5000",
    "http://develop.sung4854.com:3000",
    "https://develop.sung4854.com",
    # 추가적인 도메인들...
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    messages: Dict[str, Union[str, str]]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/chat")
async def chat(message: Message):
    print(message)
    role = message.messages['role']
    msg = message.messages['content']
    return_mes = get_chat_response(msg)
    await save_chats(role, msg) # save content to database
    return {"response": return_mes}

@app.post("/api/get_result")
async def get_result(messages: Messages):
    print(messages)
    return {"response": "success"}

@app.post("/get_job/")
async def get_job(id: int):
    job = await get_job_categories(id)
    print(job)
    return {"response": job}