from langchain_openai import ChatOpenAI
# Humam é o meu envio, System é a estrutura do agente, AI é a resposta do agente.
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.tools import tool
from langchain_core.runnables.graph import MermaidDrawMethod
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if(not API_KEY):
    raise ValueError("OPENAI_API_KEY environment variable is not set.")


llm_model = ChatOpenAI(model="gpt-3.5-turbo", api_key=API_KEY) # type: ignore

# Um agente React é um agente que pode responder a perguntas e realizar ações, a diferente de um agente de chat que apenas responde a perguntas.

system_message="Você é um assistente com acesso a ferramentas. Sempre que o usuário fizer perguntas que envolvam somar dois números, use a ferramenta 'somar', passando os dois números separados por vírgula. Caso contrário, apenas responda normalmente."
system_message = SystemMessage(content=system_message)

@tool("somar")
def somar(values: str) -> str:
    """Soma dois números inteiros separados por vírgula."""
    try:
        a, b = map(int, values.split(","))
        return str(a + b)
    except ValueError:
        raise ValueError("Valores inválidos. Certifique-se de fornecer dois números inteiros separados por vírgula.")

tools = [somar]
# Não precisa do .compile() ou add_node, pois create_react_agent já cria o grafo para você.
graph = create_react_agent(
    model=llm_model,
    tools=tools,
    prompt="Você é um assistente. Se o usuário pedir contas matemáticas, use a ferramenta 'somar'. Caso contrário, apenas responda normalmente.",
    name="agente_for_teste"
)

export_graph = graph

def extrair_resposta_final(result) -> str:
    ai_messages = [m for m in result["messages"] if isinstance(m, AIMessage) and m.content]
    if ai_messages:
        return ai_messages[-1].content # type: ignore
    return "Nenhuma resposta encontrada."


if __name__ == "__main__":
  entrada1 = HumanMessage(content="Quanto é 5 + 2?")
  result1 = export_graph.invoke({"messages": [entrada1]}) # type: ignore
  for m in result1["messages"]:
    print(m)
  resposta_text_1 = extrair_resposta_final(result1)
  print(f"Resposta 1: {resposta_text_1}")

  entrada2 = HumanMessage(content="Qual é a capital da França?")
  result2 = export_graph.invoke({"messages": [entrada2]}) # type: ignore
  for m in result2["messages"]:
    print(m)
  resposta_text_2 = extrair_resposta_final(result2)
  print(f"Resposta 2: {resposta_text_2}")

png_bytes = export_graph.get_graph().draw_mermaid_png(
    draw_method=MermaidDrawMethod.API)
with open("graph_diagram2.png", "wb") as f:
    f.write(png_bytes)