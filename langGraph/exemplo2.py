from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables.graph import MermaidDrawMethod
from langgraph.graph import StateGraph
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if(not API_KEY):
    raise ValueError("OPENAI_API_KEY environment variable is not set.")


llm_model = ChatOpenAI(model="gpt-3.5-turbo", api_key=API_KEY) # type: ignore

# Definição do StateGraph
class GraphState(BaseModel):
    input: str 
    output: str

def response_handler(state: GraphState) -> GraphState:
    input_message = state.input
    response = llm_model.invoke([HumanMessage(content=input_message)])
    return GraphState(input=input_message, output=response.content) # type: ignore

graph = StateGraph(GraphState)
graph.add_node("response", response_handler)
graph.set_entry_point("response")
graph.set_finish_point("response")

# Compilação do grafo para exportação
export_graph = graph.compile()

# Gerando o diagrama do grafo
png_bytes = export_graph.get_graph().draw_mermaid_png(
    draw_method=MermaidDrawMethod.API)
with open("graph_diagram.png", "wb") as f:
    f.write(png_bytes)