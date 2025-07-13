from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_mistralai import ChatMistralAI
chat = ChatMistralAI()
# print(chat.invoke("Olá, como você está?"))  

mensagens = [
    ("system", "Você é especialista em traduzir do português para o alemão. Traduza a frase:"),
    ("user", "Hoje é um bom dia para estudar")
]
# print(chat.invoke(mensagens))

from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "Você é um contador de anedotas em português"),
    ("user", "Crie uma história sobre: {anedota}")
])

chain = template | chat
response = chain.invoke({"anedota": "formiga e cigarra"})
# print(response.content)


# Stream the response
from langchain_core.prompts import ChatPromptTemplate
template = ChatPromptTemplate.from_messages([
    ("system", "Você é um contador de anedotas em português"),
    ("user", "Crie uma história sobre: {anedota}")
])

chain = template | chat
stream = chain.stream({"anedota": "formiga e cigarra"})
for chunk in stream:
    print(chunk.content, end="", flush=True)