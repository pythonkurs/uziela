#!/usr/bin/env python

# Written by Karolis Uziela in 2013

import requests
from dateutil import parser
from pandas import DataFrame

def test_api(my_user, my_password):
    ORG_URL = "https://api.github.com/orgs/pythonkurs"
    users = requests.get(ORG_URL + "/members", auth=(my_user, my_password))
    users_data = users.json()
    print users_data[0]

def get_commit_data_frame(my_user, my_password):
    my_names = []
    my_dates = []
    my_msgs = []
    my_messages = []
    ORG = "pythonkurs"
    repos = requests.get("https://api.github.com/orgs/%s/repos" % ORG, auth=(my_user, my_password))
    repos_data = repos.json()
    for repo in repos_data:
        repo_name = repo["name"]
        commits = requests.get("https://api.github.com/repos/%s/%s/commits" % (ORG, repo_name), auth=(my_user, my_password))
        commits_data = commits.json()
        for commit in commits_data:
            if "commit" in commit:
                commit_date = parser.parse(commit["commit"]["author"]["date"])
                commit_msg = commit["commit"]["message"]
                my_names.append(repo_name)
                my_dates.append(commit_date)
                my_msgs.append(commit_msg)

    N = len(my_msgs)
    my_df = DataFrame({"repo": my_names, "date": my_dates, "message": my_msgs}, index=range(N))
    #print my_df[0:10]
    return my_df

#def most_common_day_and_hour(my_df):



#df1 = get_commit_data_frame("uziela", "")

