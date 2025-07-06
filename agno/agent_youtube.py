from agno.agent import Agent 
from agno.tools.youtube import YouTubeTools

agent = Agent(
    show_tool_calls=True,
    tools=[YouTubeTools()],
    description="Você é um assistente que ajuda a encontrar vídeos do YouTube e extrair as legendas de um vídeo do youtube e responda às perguntas com base nessas legendas.",
)

agent.print_response("Sumarize esse vídeo: https://www.youtube.com/watch?v=WRRk-XOVfuE", markdown=True)