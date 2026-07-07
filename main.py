from agents import agent
import logging, os
from datetime import datetime
from langfuse import get_client
from langfuse.langchain import CallbackHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

log_formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

log_filename = f"app_{datetime.today().strftime('%Y-%m-%d')}.log"
file_handler = logging.FileHandler(filename=os.path.join(LOG_DIR, log_filename))
file_handler.setFormatter(log_formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[console_handler,file_handler]
)

logging.getLogger("watchfiles").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Get the configured client instance
langfuse = get_client()

# Initialize the Langfuse handler
langfuse_handler = CallbackHandler()

query = input("Enter the amount and currency you want to convert to: ")
logger.info(f"Query asked by user: {query}")
response = agent.invoke({
    "messages":[{
        "role":"user",
        "content": query
    }]
},
config={
    "callbacks":[langfuse_handler]
}
)

logger.info(f"Resulted acheived: {response}")
amount = response["messages"][-1].content
logger.info(f"Final amount after conversion: {amount}")
print(amount)
langfuse.flush()