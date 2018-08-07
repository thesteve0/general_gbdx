import csv
import requests
import json
import os
from gbdxtools import Interface

gbdx = Interface()

headers = {"Authorization":"Bearer {}".format(gbdx.catalog.gbdx_connection.access_token)}

accounts = []

page = 1

while page is not None:
    results = requests.get('https://geobigdata.io/accounts/v1/accounts?limit=100&page={}'.format(page),headers=headers).json()
    accounts =  results['accounts'] + accounts
    print(str(page) + " " + str(len(accounts)))
    page = results['next_page']

with open('gbdx-accounts.json', 'w') as f:
    f.write(json.dumps(accounts, indent=2, sort_keys=True))

