from agno.agent import Agent 
from agno.models.openai import OpenAIChat
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
    markdown=True,
)

agent.print_response("Compartilhe uma receita de bolo de cenoura com cobertura de chocolate.")

# Agno tool docs é encontrado em: https://docs.agno.com/tools/toolkits/toolkits