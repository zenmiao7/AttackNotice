import datetime
import json
import os
import requests
import uuid
from azure.cosmos import CosmosClient, PartitionKey

ENDPOINT = "https://ddosipaccount.documents.azure.com:443/"
KEY = "IJZD6EjuRNgCf64yFDavPbcXpSYxxoRAymS5jiQhJwxPhEi8XeWcj4g1UUTG8IjcSlkRrk9TGxgWACDbexlPdg=="
DATABASE_NAME = "AttackBotIP"
CONTAINER_NAME = "IPContainer"

def get_ip():
	ip_service_url = "https://ipinfo.io/ip"
	return str(requests.get(ip_service_url).text)

def upload_ip_to_cosmos(ip):
	now = datetime.datetime.utcnow()
	client = CosmosClient(url=ENDPOINT, credential=KEY)
	database = client.get_database_client(DATABASE_NAME)
	container = database.get_container_client(CONTAINER_NAME)
	container.upsert_item({
            'id': str(uuid.uuid4()),
            'ip': ip,
            'attack_time': str(now),
        }
    )

def log_ip():
	ip = get_ip()
	upload_ip_to_cosmos(ip)
	print("Logged self egress IP " + ip)