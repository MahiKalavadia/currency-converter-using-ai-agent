from langchain.agents import create_agent
from tools import exchange_rate, currency_converter
from langchain_groq import ChatGroq
from prompts import prompt
import logging

logger = logging.getLogger(__name__)

tools = [exchange_rate, currency_converter]
logger.info(f"Tools available: {tools}")

llm = ChatGroq(model="llama-3.3-70b-versatile")

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt
)