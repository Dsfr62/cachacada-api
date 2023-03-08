from fastapi import FastAPI, status
import os
import openai
from dotenv import load_dotenv
import json

from schemas import ChatGptRequestModel

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def hello():
    return {"message": "Hello world!"}


@app.post("/question", status_code=status.HTTP_200_OK)
async def question(data:ChatGptRequestModel):

    # Me retorne um objeto json com drink e suas keys são name (string), description(string), ingredients(list of an ingredient) and instructions (string array), ingredient keys are name (string) and quantity (string)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Atue como um barista e mixologista profissional com mais de 30 anos de experiencia nessa area. Com isso posto me sugira um menu de drinks feito a partir de { data.ingredients } , utilize medidas específicas do padrão { data.nacionalidade }, traduza a resposta em { data.idioma }. ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return json.loads(response.choices[0].text)
