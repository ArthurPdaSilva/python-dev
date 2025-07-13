from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
api_key = os.getenv("COHERE_API_KEY")

from langchain_cohere import ChatCohere
chat = ChatCohere(
    cohere_api_key=api_key,     # type: ignore
    model="command-r-plus",
    temperature=1,
)

print(chat.invoke("Quem é você?")) 

from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "Você é um contador de histórias"),
    ("user", "Conte uma história sobre {conteudo} com até {n_palavras} palavras")
])

chain = template | chat
# response = chain.invoke({"conteudo": "análise de dados", "n_palavras":20})
# print(response.content)

# response = chain.invoke({"conteudo": "data science", "n_palavras": 30})
# print(response.content)

# stream = chain.stream({"conteudo": "inteligência artificial", "n_palavras": 500})
# for chunk in stream:
#     print(chunk.content, end="", flush=True)