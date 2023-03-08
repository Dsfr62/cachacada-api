from pydantic import BaseModel
from typing import List

class ChatGptRequestModel(BaseModel):
    ingredients: List[str]
    nacionalidade: str
    idioma:str
