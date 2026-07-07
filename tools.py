from langchain_core.tools import tool
from dotenv import load_dotenv
import logging, requests,os

load_dotenv()

logger = logging.getLogger(__name__)

@tool
def exchange_rate(base_currency:str, target_currency:str):
    """Takes the base currency and target currency from user and identify the conversion rate"""
    api_key=os.environ.get("api_key")
    base_url=f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    logger.info(f"Received base currency and target currency: {base_currency} to {target_currency}")
    response = requests.get(base_url).json()
    logger.info(f"Response received: {response}")
    return response

@tool
def currency_converter(base_currency_value:int, conversion_rate:float):
    """They have the conversion rate so multipies the conversion rate to the base currency value"""
    value = conversion_rate * base_currency_value
    logger.info(f"Converting the value: {conversion_rate}*{base_currency_value}")
    return round(value, ndigits=2)