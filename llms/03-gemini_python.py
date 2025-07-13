from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
api_key = os.getenv("GEMINI_API_KEY")

import textwrap
def format_text(response):
    text = response
    print(textwrap.fill(text, width=100))

import google.generativeai as genai
genai.configure(api_key=api_key) # type: ignore
model = genai.GenerativeModel("gemini-1.5-flash")  # type: ignore
response = model.generate_content("Qual dica para quem é iniciante em Python?")
format_text(response.text)



# Stream the response
stream = model.generate_content("Explique sobre o iluminismo", stream=True)  
# for chunk in stream:
    # print(chunk.text, end="", flush=True)


# Imagens
import httpx
import os
import base64

model = genai.GenerativeModel(model_name="gemini-1.5-pro") # type: ignore
image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ1e2zbNML3dqInuia63pwOxf2IXpw0Y-LoA&s"
image = httpx.get(image_path)

prompt = "Descreva a imagem para mim"
response = model.generate_content([
    {"mime_type": "image/jpeg",
     "data": base64.b64encode(image.content).decode("utf-8")},
    prompt
])
# print(response.text)

# Histórico de chat
model = genai.GenerativeModel("gemini-1.5-flash") # type: ignore
chat = model.start_chat(history=[])
response = chat.send_message("Explique o que é LangChain para uma criança")
response = chat.send_message("Agora explique para um adulto")
# format_text(response.text)