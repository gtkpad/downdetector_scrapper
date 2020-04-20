#!/bin/python3
#########################################
#                                       #
# Author: Gabriel Padilha               #
# Email: gabrielvargaspadilha@gmail.com #
#                                       #
#########################################
import cloudscraper
import sys
import re
from bs4 import BeautifulSoup


def parse_result(status_text):
    if status_text == 'success':
        status_number = 1
    if status_text == 'warning':
        status_number = 2
    if status_text == 'danger':
        status_number = 3
    else:
        status_number = 0
    print(status_number)
    exit()


if len(sys.argv) < 2:
    print("Informe o site que gostaria de verificar")
    sys.exit(1)
site = sys.argv[1]

scraper = cloudscraper.create_scraper()
response = scraper.get("https://downdetector.com.br/fora-do-ar/{}/".format(site))

if response.status_code != 200:
    print(0)
    exit()

bs = BeautifulSoup(response.text, 'html.parser')
dataParse = bs.find("div", {"class": "entry-title"})
status = dataParse.attrs["class"][2].split('-')[1]

if status not in ['success', 'warning', 'danger']:
    parse_result(status)
else:
    failover = re.compile(".*status: '(.*)',.*", re.MULTILINE)
    failover_status = failover.findall(response.text).pop()
    parse_result(failover_status)
