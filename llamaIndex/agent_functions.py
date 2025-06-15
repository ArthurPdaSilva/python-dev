# ====================================
# IMPORTS E CONFIGURAÇÕES INICIAIS
# ====================================

import os
from dotenv import load_dotenv, find_dotenv
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    Settings,
    StorageContext,
    load_index_from_storage,
)
from llama_index.llms.groq import Groq
from llama_index.core.tools import FunctionTool, QueryEngineTool, ToolMetadata
from llama_index.core.agent import (
    FunctionCallingAgentWorker,
    AgentRunner,
    ReActAgent,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.tools.tavily_research import TavilyToolSpec
import arxiv

load_dotenv(find_dotenv())

# ====================================
# LLM SETUP
# ====================================

llm = Groq(
    model="llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY"),
)

# ====================================
# FERRAMENTA 1: CÁLCULO DE IMPOSTO
# ====================================

def calcular_imposto_renda(rendimento: float) -> str:
    if rendimento <= 22847.76:
        return "Isento de Imposto de Renda"
    elif rendimento <= 33919.80:
        imposto = (rendimento - 22847.76) * 0.075
    elif rendimento <= 45012.60:
        imposto = (rendimento - 33919.80) * 0.15 + 826.29
    elif rendimento <= 55976.16:
        imposto = (rendimento - 45012.60) * 0.225 + 1428.14
    else:
        imposto = (rendimento - 55976.16) * 0.275 + 2203.91

    return f"Imposto de Renda devido: R$ {imposto:.2f}"

ferramenta_calculo_imposto = FunctionTool.from_defaults(
    fn=calcular_imposto_renda,
    name="calcular_imposto_renda",
    description=(
        "Calcula o Imposto de Renda devido com base no rendimento anual. "
        "Argumento: rendimento (float). Retorna isenção ou valor devido."
    ),
)

# ====================================
# FERRAMENTA 2: CONSULTA ARXIV
# ====================================

def consulta_artigos(title: str) -> str:
    buscar = arxiv.Search(
        query=title,
        max_results=5,
        sort_by=arxiv.SortCriterion.Relevance,
    )
    resultados = [
        f"Título: {artigo.title}\nCategoria: {artigo.primary_category}\nLink: {artigo.entry_id}"
        for artigo in buscar.results()
    ]
    return "\n\n".join(resultados) if resultados else "Nenhum artigo encontrado."

consulta_artigos_tool = FunctionTool.from_defaults(
    fn=consulta_artigos,
    name="consulta_artigos",
    description=(
        "Consulta artigos no ArXiv com base no título fornecido. "
        "Argumento: title (str). Retorna artigos encontrados."
    ),
)

# ====================================
# FERRAMENTA 3: TAVILY TOOL (Pesquisa na Web)
# ====================================

tavily_api_key = os.environ.get("TAVILY_API_KEY")
tavily_tool = TavilyToolSpec(api_key=tavily_api_key)  # type: ignore

tavily_tool_function = FunctionTool.from_defaults(
    fn=tavily_tool.search,
    name="tavily_search",
    description=(
        "Busca artigos e informações na web usando Tavily. "
        "Argumento: query (str). Retorna uma lista de resultados relevantes."
    ),
)

# ====================================
# AGENTS COM FERRAMENTAS FUNCIONAIS
# ====================================

agent_worker_funcional = FunctionCallingAgentWorker.from_tools(
    llm=llm,
    tools=[ferramenta_calculo_imposto, consulta_artigos_tool, tavily_tool_function],
    verbose=True,
    allow_parallel_tool_calls=False,
)

agent_funcional = AgentRunner(agent_worker_funcional)

# ====================================
# LEITURA DE DOCUMENTOS PDF
# ====================================

artigo = SimpleDirectoryReader(input_files=["files/LLM.pdf"]).load_data()
tutorial = SimpleDirectoryReader(input_files=["files/LLM_2.pdf"]).load_data()

# ====================================
# EMBEDDING COM HUGGINGFACE
# ====================================

Settings.embed_model = HuggingFaceEmbedding(
    model_name="intfloat/multilingual-e5-large"
)

artigo_index = VectorStoreIndex.from_documents(artigo)
tutorial_index = VectorStoreIndex.from_documents(tutorial)

artigo_index.storage_context.persist(persist_dir="artigo")
tutorial_index.storage_context.persist(persist_dir="tutorial")

# ====================================
# RECARREGAMENTO DOS ÍNDICES
# ====================================

artigo_index = load_index_from_storage(
    storage_context=StorageContext.from_defaults(persist_dir="artigo")
)
tutorial_index = load_index_from_storage(
    storage_context=StorageContext.from_defaults(persist_dir="tutorial")
)

# ====================================
# CRIAÇÃO DAS ENGINES DE BUSCA
# ====================================

artigo_engine = artigo_index.as_query_engine(similarity_top_k=3, llm=llm)
tutorial_engine = tutorial_index.as_query_engine(similarity_top_k=3, llm=llm)

query_engine_tools = [
    QueryEngineTool(
        query_engine=artigo_engine,
        metadata=ToolMetadata(
            name="artigo_engine",
            description="Fornece informações sobre LLM e LangChain."
        )
    ),
    QueryEngineTool(
        query_engine=tutorial_engine,
        metadata=ToolMetadata(
            name="tutorial_engine",
            description="Fornece informações sobre aplicações de LLMs."
        )
    ),
]

# ====================================
# AGENT COM DOCUMENTOS (FunctionCalling)
# ====================================

agent_worker_docs = FunctionCallingAgentWorker.from_tools(
    query_engine_tools,  # type: ignore
    verbose=True,
    allow_parallel_tool_calls=True,
    llm=llm
)

agent_document = AgentRunner(agent_worker_docs)

# ====================================
# AGENT COM DOCUMENTOS (ReAct) - ReAct Agent é mais adequado para tarefas de consulta
# ====================================

react_agent = ReActAgent.from_tools(
    query_engine_tools,  # type: ignore
    verbose=True,
    llm=llm,
)

# EXEMPLO DE USO:
response = react_agent.chat(
    "Quais são os casos de uso e aplicações de LLMs?"
)

# print(response)

# =========================
# EXEMPLO: AGENTE DE IMPOSTO
# =========================

# response = agent_imposto.chat(
#     "Qual é o imposto de renda devido para um rendimento anual de R$ 50000.00?",
# )

# =========================
# EXEMPLO: CONSULTA ARXIV
# =========================

# response2 = agent.chat(
#     "Quais artigos existem sobre 'Machine Learning'?",
# )

# =========================
# EXEMPLO: TAVILY TOOL
# =========================

# response3 = agent.chat(
#     "Me retorne artigos sobre 'Machine Learning'",
# )

# =========================
# EXEMPLO: DOCUMENTOS (FunctionCalling)
# =========================

# response = agent_document.chat(
#     "Quais as principais aplicações posso construir com LLM e LangChain?",
# )

# response = agent_document.chat(
#     "Quais são os casos de uso e aplicações de LLMs?",
# )

