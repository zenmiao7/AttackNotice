#!/bin/bash
sudo apt-get update
sudo apt install slowhttptest python3-pip git python3-azure-cosmos python3-requests -y

git clone https://github.com/zenmiao7/AttackNotice/
cd AttackNotice/
python3 logIP.py
python3 main.py