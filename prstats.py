#!/usr/bin/env python

import requests
# import getpass
# import argparse
# import prstats_config as pc

# # parsing arguments
# arguments = argparse.ArgumentParser(description='Get Pull Request statistic from GitHub')
# arguments.add_argument('-i', nargs='?', help='Set update interval (in seconds).')
# args = arguments.parse_args()

# # parsing config file
# logFile = pc.config['logFile']
# interval = int(args.i if args.i else pc.config['interval'])

# # clear log file
# f = open(logFile, "w")
# f.write("")
# f.close()

import pullrequest

user = 'alenaPy'
repo = 'devops_lab'
token = 'f63642c4677fd4ebf2f3b586133f623a614ce90b'

def getprlists(user, repo):
    pr = []
    # using for loop because of paging of github-output
    for i in range(1, 100):
        url = 'https://api.github.com/repos/{user}/{repo}/pulls/{PRNUMBER}/comments?page={i}&per_page=100&state=all'.\
            format(user=user, repo=repo, i=i, PRNUMBER=37)
        headers = {'Authorization': 'token %s' % token}
        currentPage = (requests.get(url, headers=headers)).json()
        if len(currentPage) == 0:
            return pr
        pr.extend(currentPage)


for i in pullrequest.getAllPR(user, repo):
    print(i)



#
# pulls_list = getprlists(user, repo)
#
# f = open('answer.json', 'w')
# for i in pulls_list:
#
#     print(i)
#     for k, v in i.items():
#         # print("%s : %s" % (k, v))
#         f.write("%s : %s" % (k, v))
#         f.write('\n')
#
# # print(pulls_list)
# f.close()
#
#
# # comments list
# # https://api.github.com/repos/{user}/{repo}/pulls/{PRNUMBER}/comments?page=1&per_page=100&state=all



