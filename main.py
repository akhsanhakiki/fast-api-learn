from tkinter.messagebox import NO
from fastapi import FastAPI
from pydantic import BaseModel, NonNegativeFloat
from typing import Optional

import json

app = FastAPI()

class person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str
    
with open('people.json', 'r') as f:
    people = json.load(f)
    
@app.get('/people')
def hello_get():
    return people