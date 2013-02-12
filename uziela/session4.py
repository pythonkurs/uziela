#!/usr/bin/env python

# Written by Karolis Uziela in 2013

import requests


def test_api(my_user, my_password):
    ORG_URL = "https://api.github.com/orgs/pythonkurs"
    users = requests.get(ORG_URL + "/members", auth=(my_user, my_password))
    users_data = users.json()
    print users_data[0]


