import csv
import requests
import json
import os
from gbdxtools import Interface

gbdx = Interface()

headers = {"Authorization":"Bearer {}".format(gbdx.catalog.gbdx_connection.access_token)}

users = []

page = 1

while page is not None:
    results = requests.get(' https://geobigdata.io/users/v1/users?per_page=100&page={}'.format(page),headers=headers).json()
    users = results['users'] + users
    print(str(page) + " " + str(len(users)))
    page = results['next_page']

with open('gbdx-users.json', 'w') as f:
    f.write(json.dumps(users, indent=2, sort_keys=True))