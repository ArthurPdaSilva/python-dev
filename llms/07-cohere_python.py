from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
import cohere
client = cohere.Client(os.getenv("COHERE_API_KEY"))

model = "command-r-plus"
response = client.chat(
    model=model,
    message="Quam é você?",
)
# print(response.text)

# Stream the response
response = client.chat_stream(
    model=model,
    message="Explique sobre a torre de babel",
)
# for chunk in response:
#     if chunk.event_type == "text-generation":
#         print(chunk.text, end="", flush=True)


# Criando histórico de mensagens
history = [
    {"role": "USER", "text": "Quem é você?"},
    {"role": "CHATBOT", "text": "Eu sou um assistente virtual."},
    {"role": "USER", "text": "Qual é a capital da França?"},
    {"role": "CHATBOT", "text": "A capital da França é Paris."},
]

stream = client.chat_stream(
    model=model,
    message="Qual era a capital do país mesmo?",
    chat_history=history, # type: ignore
)

for chunk in stream:
    if chunk.event_type == "text-generation":
        print(chunk.text, end="", flush=True)
