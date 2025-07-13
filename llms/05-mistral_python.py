from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
api_key = os.getenv("MISTRAL_API_KEY")

from mistralai import Mistral
client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model="mistral-large-latest",
    messages=[
        {
            "role": "user",
            "content": "Explique o que é o Mistral e como ele pode ser usado para executar modelos de linguagem. Responda em português."
        }
    ]
)
# print(chat_response.choices[0].message.content)  # type: ignore


# Vision
model = "pixtral-12b-2409"
messages = [
    {
        "role": "user",
        "content":[
            {
                "type": "text",
                "text": "Descreva para mim essa imagem"
            },
            {
                "type": "image_url",
                "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ1e2zbNML3dqInuia63pwOxf2IXpw0Y-LoA&s"
            }
        ]
    }
]

chat_response = client.chat.complete(
    model=model,
    messages=messages # type: ignore
)

# print(chat_response.choices[0].message.content)


# Code Generation
model = "codestral-mamba"
messages = [
    {
        "role": "user",
        "content": "Escreva uma função em Assembly que some dois números inteiros e retorne o resultado. Comente o código explicando cada parte."
    }
]

chat_response = client.chat.complete(
    model=model,
    messages=messages # type: ignore
)

# print(chat_response.choices[0].message.content)  # type: ignore