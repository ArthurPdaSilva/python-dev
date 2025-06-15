import json 
import os 
from datetime import datetime, timedelta
from crewai import Agent, Task, Crew, Process 
from crewai_tools import CSVSearchTool
from crewai.tools import BaseTool
from dotenv import load_dotenv, find_dotenv
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_openai import ChatOpenAI 
from IPython.display import display, Markdown

load_dotenv(find_dotenv())


csv_imoveis = CSVSearchTool(csv="files/imoveis.csv")

corretor_imoveis = Agent(
    role="Corretor de Imóveis",
    goal="Obtenha as preferências do cliente e busque imóveis compatíveis no banco de dados",
    backstory="Especialista no mercado imobiliário, encontra as melhores opções baseadas no perfil do cliente",
    verbose=True,
    allow_delegation=False,
    max_iter=5,
    tools=[csv_imoveis],
    memory=True,
)

buscar_imoveis = Task(
    description="Pesquise imóveis na região desejada pelo cliente, considerando a faixa de preço e tipo de imóveis",
    expected_output="Lista de imóveis disponíveis com detalhes sobre a localização, preço e características",
    agent=corretor_imoveis
)


analista_de_mercado = Agent(
    role="Analista de mercado imobiliário",
    goal="Analisa tendências de preços e ajuda a prever a valorização ou desvalorização de imóveis na cidade {cidade}",
    backstory="Experiente no setor, usa dados históricos para prever preços futuros",
    verbose=True,
    allow_delegation=False,
    max_iter=5,
    memory=True,
)

def obter_precos_imoveis(cidade: str = "geral"):
    precos = {
        "São Paulo": {"tendencia":"aumento", "percentual":5.2},
        "Rio de Janeiro": {"tendencia":"estavel", "percentual": 0.0},
        "Belo Horizonte": {"tendencia":"queda", "percentual":-3.1},
        "geral": {"tendencia":"aumento", "percentual":4.0} 
    }
    return precos.get(cidade, precos["geral"])

class TendenciaPrecosImoveisTool(BaseTool):
    name: str = "Analisador de Preços Imobiliários"
    description: str = "Obtém tendências de preços de imóveis com base na cidade especificada."
    
    def _run(self, cidade: str) -> dict:
        """
        Executa a análise de preços imobiliários e retorna a tendência com base na cidade.
        """
        try:
            return obter_precos_imoveis(cidade)
        except Exception as e:
            return {"erro": f"Erro ao obter tendências de preços {str(e)}"}
        

obter_tendencias = Task(
    description="""
    Analisa o histórico de preços de imóveis na cidade {cidade} e forneça insights sobre
    valorização ou desvalorização. Considere o tipo de imóvel {tipo_imovel} e a
    faixa de preço {faixa_preco}""",
    expected_output="Resumo da tendência dos preços no mercado imobiliário",
    tools=[TendenciaPrecosImoveisTool()],
    agent=analista_de_mercado,
    parameters=["cidade"]
)


analista_noticias = Agent(
    role="Analista de Notícias Imobiliários",
    goal="Busca notícias relevantes sobre o mercado imobiliário para avaliar fatores externos.",
    backstory="Especialista em analisar notícias e tendências econômicas que afetam os preços dos imóveis",
    verbose=True,
    allow_delegation=False,
    max_iter=5,
    memory=True,
)

searchTool = DuckDuckGoSearchResults(backend="news", num_results=5)

buscar_noticias = Task(
    description=f"Pesquise notícias recentes sobre o mercado imobiliário. Data atual {datetime.now}",
    expected_output="Resumo das principais notícias e tendências imobiliárias",
    agent=analista_noticias,
    tool=[searchTool]
)

consultor_financeiro = Agent(
    role="Consultor Financeiro",
    goal="Analisa opções de financiamento imobiliário com base no perfil do cliente.",
    backstory="Especialista em crédito imobiliário, ajuda clientes a escolherem as melhores opções de financiamento",
    verbose=True,
    allow_delegation=False,
    max_iter=5,
    memory=True
)

calcular_financiamento = Task(
    description="Analise a renda do cliente e sugira opções de financimaneto viáveis.",
    expected_output="Tabela comparativa com diferentes financiamentos, taxa de juros e prazos",
    agent=consultor_financeiro
)

redator = Agent(
    role="Redator de Relatórios Imobiliários",
    goal="Gera um relatório completo e persuasivo com base nas análises de mercado e imóveis encontrados.",
    backstory="Especialista em comunicação, traduz dados complexos para clientes de forma clara e objetiva.",
    verbose=True,
    allow_delegation=False,
    max_iter=5,
    memory=True
)

gerar_relatorio = Task(
    description="Gere um relatório detalhado sobre o melhor imóvel encontrado, considerando preços, tendências e financiamento.",
    expected_output="Relatório formatado com resumo do mercado, opções recomendadas e justificativa da escolha.",
    agent=redator,
    context=[buscar_imoveis, obter_tendencias, buscar_noticias, calcular_financiamento]
)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

crew = Crew(
    agents=[corretor_imoveis, analista_de_mercado, analista_noticias, consultor_financeiro, redator],
    tasks=[buscar_imoveis, obter_tendencias, buscar_noticias, calcular_financiamento, gerar_relatorio],
    verbose=True,
    process=Process.hierarchical,
    full_output=True,
    share_crew=False,
    max_iter=15,manager_llm=llm
)

result = crew.kickoff(inputs={
    "cidade": "Rio de Janeiro",
    "tipo_imovel": "Apartamento",
    "faixa_preco": "500000-700000"
})


display(Markdown(str(result)))