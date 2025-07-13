from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from groq import Groq
client = Groq()

messages = [
    {
        "role": "user",
        "content": "Explique o que é o Groq e como ele pode ser usado para executar modelos de linguagem. Responda em português."
    }
]

response = client.chat.completions.create(
    messages=messages, # type: ignore
    model="llama3-8b-8192",
)


# print(response.choices[0].message.content)  # type: ignore


# Stream the response
response2 = client.chat.completions.create(
    messages=messages, # type: ignore
    model="llama3-8b-8192",
    stream=True,
)

# for chunk in response2:
    # print(chunk.choices[0].delta.content, end="", flush=True)  # type: ignore


# Transcribe audio
import textwrap

def format_text(response):
    text = response.text
    print(textwrap.fill(text, width=100))

file = "files/curso.mp3"

# with open(file, "rb") as audio_file:
#     response = client.audio.transcriptions.create(
#         file=(file, audio_file.read()),
#         model="whisper-large-v3",
#         response_format="json",
#         language="pt",
#         prompt="Transcreva o áudio a seguir para o português. Este é um curso de Hugging Face que usa aplicação com o Gradio",
#     )

#     format_text(response)


# Vision
def format_text_v2(response):
    text = response.content
    print(textwrap.fill(text, width=100))

completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[{
        "role": "user",
        "content":[
            {"type": "text", "text":"O que há nessa imagem?"},
            {"type":"image_url", "image_url": {
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ1e2zbNML3dqInuia63pwOxf2IXpw0Y-LoA&s"
            }}
        ]
    }],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None
)

format_text_v2(completion.choices[0].message)  # type: ignore