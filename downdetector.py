#!/usr/bin/python3
#########################################
#                                       #
# Author: Gabriel Padilha               #
# Email: gabrielvargaspadilha@gmail.com #
#                                       #
#########################################
import sys
import ssl
import re
import random
from bs4 import BeautifulSoup
if ssl.OPENSSL_VERSION_INFO[0] < 1 or ssl.OPENSSL_VERSION_INFO[1] < 1 or ssl.OPENSSL_VERSION_INFO[2] < 1:
    user_agent_list = [
        # Chrome
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 '
        'Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 '
        'Safari/537.36',
        # Firefox
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; '
        '.NET CLR 3.5.30729) '
    ]
    import requests
    craw = "requests"
else:
    import cloudscraper
    craw = "cloudscraper"


def request(dd_site):
    url = "https://downdetector.com.br/fora-do-ar/{}/".format(dd_site)
    if not craw:
        print(0)
        exit()
    elif craw == "cloudscraper":
        scraper = cloudscraper.create_scraper()
        return scraper.get(url)
    else:
        return requests.get(url, headers={'User-Agent': random.choice(user_agent_list)})


def parse_result(status_text):
    status_text = status_text.strip()
    if status_text == 'success':
        status_number = 1
    elif status_text == 'warning':
        status_number = 2
    elif status_text == 'danger':
        status_number = 3
    else:
        status_number = 0
    print(status_number)
    exit()


if len(sys.argv) < 2:
    print("Informe o site que gostaria de verificar")
    sys.exit(1)
site = sys.argv[1]

response = request(site)

if response.status_code != 200:
    print(0)
    exit()

bs = BeautifulSoup(response.text, 'html.parser')
dataParse = bs.find("div", {"class": "entry-title"})
status = dataParse.attrs["class"][2].split('-')[1]

if status in ['success', 'warning', 'danger']:
    parse_result(status)
else:
    failover = re.compile(".*status: '(.*)',.*", re.MULTILINE)
    failover_status = failover.findall(response.text).pop()
    parse_result(failover_status)
