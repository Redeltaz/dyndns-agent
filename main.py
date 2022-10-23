import os

from src.agent import Agent
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")
APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
ZONE_NAME = os.getenv("ZONE_NAME")
APP_ID = os.getenv("APP_ID")

if __name__ == "__main__":
    if not os.path.exists("/var/log/dyndns/agent.log"):
        print("No log file detected, please create one by following the GitHub repository documentation")
        exit()

    ovh_dyndns = Agent(ENDPOINT, APP_KEY, APP_SECRET, CONSUMER_KEY, ZONE_NAME, int(APP_ID))
    ovh_dyndns.start_agent()
