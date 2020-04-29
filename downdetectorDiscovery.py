#!/bin/python3
import os
import sys
import json
# FILE = "/usr/lib/zabbix/externalscripts/downdetectorlist.list"
FILE = "downdetectorlist.list"

if not os.path.isfile(FILE):
    print("File not found")
    sys.exit()

file = open(FILE, "r")

data = {
    "data": []
}

for line in file.readlines():
    line_data = line.rstrip().split(';')
    if line_data[0] == '1':
        dic = {"{#SITE_ID}": line_data[1], "{#SITE_NOME}": line_data[2]}
        data['data'].append(dic)

print(json.dumps(data))