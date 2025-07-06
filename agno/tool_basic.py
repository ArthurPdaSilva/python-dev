from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

def get_openai_api_key():
    """
    Retrieves the OpenAI API key from environment variables.
    """
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    return openai_api_key

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-mini",
        api_key=get_openai_api_key()
    ),
    tools=[YFinanceTools(stock_price=True)], # Habilita consulta de preço de ações
    markdown=True,
)

agent.print_response("Qual o preço da ação da Wege?")

# Agno tool docs é encontrado em: https://docs.agno.com/tools/toolkits/toolkits