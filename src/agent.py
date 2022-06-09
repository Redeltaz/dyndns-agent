import os
import requests
import time
from datetime import datetime

import ovh
from ovh import Client

class Agent:
    __ovh_client: Client
    __zone_name: str
    __app_id: int

    def __init__(self, endpoint: str, app_key: str, app_secret: str, consumer_key: str, zone_name: str, app_id: int) -> None:
        """
        Init OVH client
        """
        self.__zone_name = zone_name
        self.__app_id = app_id

        self.__ovh_client = ovh.Client(
            endpoint=endpoint,
            application_key=app_key,
            application_secret=app_secret,
            consumer_key=consumer_key
        )

    def __change_domain_target(self, ip: str):
        """
        Change domain target with OVH API, also update old ip file

        :param ip: new ip to use on domain target
        """
        try:
            self.__ovh_client.put(f"/domain/zone/{self.__zone_name}/record/{self.__app_id}",
                subDomain="home",
                target=ip
            )

            file = open("src/last_ip.txt", "w")
            file.write(ip)
            file.close()
        except:
            self.__append_log("Error when updating OVH domain entry")

    def __get_current_ip(self):
        """
        Get current public IP by requesting an API

        :return: your actual public ip
        """
        #TODO: Error handling on ip request
        response = requests.get("https://api.ipify.org?format=json")
        current_ip = response.json()["ip"]

        return current_ip

    def __append_log(self, message: str):
        """
        Add message content to log file located on /var/log/dyndns-agent.log

        :param message: message content to add to log file
        """
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        try:
            log_file = open("/var/log/dyndns-agent.log", "a")
            log_file.write(current_date + " - " + message + "\n")
            log_file.close()
        except:
            print("Error when writing on log file")

    def start_agent(self):
        """
        Start DynDNS process by checking public IP change every 60 seconds
        """
        print("Starting DynDNS Agent")

        while True:
            current_ip = self.__get_current_ip()

            file = open("src/last_ip.txt", "r")
            previous_ip = file.readline()

            if current_ip != previous_ip:
                self.__append_log(f"Public IP changed from {previous_ip} to {current_ip}")
                self.__change_domain_target(current_ip)
            else:
                self.__append_log(f"Public IP didn't change, still {current_ip}")

            time.sleep(60)
