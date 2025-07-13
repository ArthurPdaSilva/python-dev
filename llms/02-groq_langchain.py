from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_groq import ChatGroq
chat = ChatGroq(
    temperature=0,
    model="llama3-8b-8192",
)

response = chat.invoke("Oi! Responda em português: O que é o Groq e como ele pode ser usado para executar modelos de linguagem?")
# print(response.content) 

# Formatar outputs:
import textwrap
def format_text(response):
    text = response
    print(textwrap.fill(text, width=100))


from langchain_core.prompts import ChatPromptTemplate
template = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente que sempre fala no sentido figurado e sempre tentando fazer referência a algo relacionado a vida na roça em Santa Luzia na Paraíba."),
    ("human", "{input}")
])

chain = template | chat
response = chain.invoke({"input": "O que é o céu?"})
# format_text(response.content)


# Stream the response
stream = chain.stream({"input": "Só os loucos sabem não é mesmo?"})
# for chunk in stream:
    # print(chunk.content, end="", flush=True)


# Tool 
from typing import Optional
from langchain_core.tools import tool
from datetime import datetime

@tool
def hora_atual(formato: Optional[str] = "%H:%M:%S") -> str:
    """
    Retorna a hora atual no formato especificado.
    Se nenhum formato for especificado, retorna no formato padrão 'HH:MM:SS'.
    """
    if formato is None:
        return datetime.now().strftime("%H:%M:%S")
    return datetime.now().strftime(formato)

chat_with_tool = chat.bind_tools([hora_atual], tool_choice="auto")
responsev5 = chat_with_tool.invoke("Qual é a hora atual? Me fale no formato 'HH:MM:SS'.")
print(responsev5)  