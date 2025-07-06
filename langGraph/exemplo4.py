from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
from langchain_core.runnables.graph import MermaidDrawMethod
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if(not API_KEY):
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Inicializar o modelo LLM com a chave da API
llm_model = ChatOpenAI(model="gpt-3.5-turbo", api_key=API_KEY) # type: ignore


# Definição do StateGraph
class GraphState(BaseModel):
    input: str 
    output: str
    type: str | None = None 

# Função de realizar cálculo
def realizar_calculo(state: GraphState) -> GraphState:
    return GraphState(
        input=state.input, 
        output="Resposta do cálculo fictício é 42"
    )

# Função de responder perguntas normais
def responder_curiosidades(state: GraphState) -> GraphState:
    return GraphState(
        input=state.input, 
        output=llm_model.invoke([HumanMessage(content=state.input)]).content, # type: ignore
    )

#  Função de perguntas não reconhecidas 
def pergunta_nao_reconhecida(state: GraphState) -> GraphState:
    return GraphState(
        input=state.input, 
        output="Desculpe, não entendi a pergunta."
    )

# Função de classificação de nodes
def classificar_pergunta(state: GraphState) -> GraphState:
    pergunta = state.input.lower()
    if any(termo in pergunta for termo in ["quanto é", "soma", "calcule", "+", "adição", "calcular"]):
        state.type = "calculo"
    elif any(termo in pergunta for termo in ["qual é", "quem é", "onde é", "como é", "por que é", "curiosidade"]):
        state.type = "curiosidade"
    else:
        state.type = "desconhecido"
    return state


# Criando o Graph e adicionando os nodes
graph = StateGraph(GraphState)
graph.add_node("classificar_pergunta", classificar_pergunta)
graph.add_node("responder_curiosidades", responder_curiosidades)
graph.add_node("realizar_calculo", realizar_calculo)
graph.add_node("pergunta_nao_reconhecida", pergunta_nao_reconhecida)

# Adicionando condições
graph.add_conditional_edges(
    "classificar_pergunta",
    lambda state: state.type,
    {
        "calculo": "realizar_calculo",
        "curiosidade": "responder_curiosidades",
        "desconhecido": "pergunta_nao_reconhecida",
    }
)

# Definindo o ponto de entrada e de saída
graph.set_entry_point("classificar_pergunta")
graph.set_finish_point(["responder_curiosidades", "realizar_calculo", "pergunta_nao_reconhecida"]) # type: ignore
export_graph = graph.compile()

# Testando o grafo
if __name__ == "__main__":
    exemplos = [
        "Quanto é 5 + 2?",
        "Qual é a capital da França?",
        "Quem é o presidente dos EUA?",
        "Calcule 10 * 3",
        "O que é inteligência artificial?",
        "Pergunta sem sentido"
    ]

    for exemplo in exemplos:
        resultado = export_graph.invoke(GraphState(input=exemplo, output=""))
        print(f"Pergunta: {exemplo}, Resposta: {resultado["output"]}")

png_bytes = export_graph.get_graph().draw_mermaid_png(
    draw_method=MermaidDrawMethod.API)
with open("graph_diagram4.png", "wb") as f:
    f.write(png_bytes)