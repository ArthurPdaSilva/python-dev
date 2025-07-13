from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
import atexit
import gc

api_key = os.getenv("GEMINI_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

chat = ChatGoogleGenerativeAI(
    google_api_key=api_key,  # type: ignore
    model="gemini-1.5-flash",
    temperature=0,
)

template = ChatPromptTemplate.from_messages([
    ("system", "Você é um um tradutor de português para inglês. Você é usa gírias gauchas sempre bem humorado.Agora, traduza o seguinte texto:"),
    ("human", "{input}")
])


chain = template | chat
response = chain.invoke({"input": "O que é o céu?"}) # type: ignore
# print(response.content)

# Stream the response
stream = chain.stream({"input": "Explique sobre o iluminismo"})  # type: ignore
for chunk in stream:
    print(chunk.content, end="", flush=True)

