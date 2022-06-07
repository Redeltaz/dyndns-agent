import os

import ovh
from ovh import Client

from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")
APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
ZONE_NAME = os.getenv("ZONE_NAME")
ID = os.getenv("ID")

class Agent:
    __ovh_client: Client
    __zone_name: str
    __id: int

    def __init__(self, endpoint: str, app_key: str, app_secret: str, consumer_key: str, zone_name: str, id: int) -> None:
        self.__zone_name = zone_name
        self.__id = id

        self.__ovh_client = ovh.Client(
            endpoint=endpoint,
            application_key=app_key,
            application_secret=app_secret,
            consumer_key=consumer_key
        )

        print("Welcome", self.__ovh_client.get('/me')['firstname'])
        #self.__ovh_client.put(f"/domain/zone/{self.__zone_name}/record/{self.__id}",
        #    subDomain="home",
        #    target="8.8.8.8"
        #)

if __name__ == "__main__":
    ovh_dyndns = Agent(ENDPOINT, APP_KEY, APP_SECRET, CONSUMER_KEY, ZONE_NAME, int(ID))
