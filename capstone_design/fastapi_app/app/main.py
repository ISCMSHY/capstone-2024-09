from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Request
from pydantic import BaseModel
from .open_ai import get_chat_response
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
from typing import List, Dict, Union

router = APIRouter()
app = FastAPI()

origins = [
    "http://react_app:3000",  # React 앱의 도메인
    "http://fastapi_app:5000",
    # 추가적인 도메인들...
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "mysql+pymysql://root:root@mysql_db/consult_data"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Message(BaseModel):
    messages: Dict[str, Union[str, str]]
class Messages(BaseModel):
    messages: List[Message]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/chat")
async def chat(message: Message):
    print(message)
    role = message.messages['role']
    msg = message.messages['content']
    return_mes = get_chat_response(msg)

    session = SessionLocal()
    try:
        metadata = MetaData()
        chats = Table('chats', metadata, autoload_with=engine)
        query = chats.insert().values(role=role, content=msg)
        session.execute(query)
        session.commit()
    finally:
        session.close()

    return {"response": return_mes}

@app.post("/api/get_result")
async def get_result(messages: Messages):
    print(messages)
    return {"response": "success"}

@app.get("/employees/")
def read_employees():
    session = SessionLocal()
    try:
        metadata = MetaData()
        employees = Table('employees', metadata, autoload_with=engine)
        query = select(employees)
        result = session.execute(query)
        print(result)
        # Convert ResultProxy to a list of dictionaries
        result_as_dict = [row._asdict() for row in result]
        return result_as_dict
    finally:
        session.close()