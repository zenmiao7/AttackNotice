#!/bin/bash

sudo apt-get update
sudo apt install slowhttptest python3-pip git -y
pip install requests azure-cosmos

git clone https://github.com/zenmiao7/AttackNotice/
cd AttackNotice/
python3 logIP.py
python3 main.py