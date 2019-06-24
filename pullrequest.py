import requests
from datetime import datetime
import getpass

username = input("Please enter your GitHub name: ")
password = getpass.getpass(prompt="Enter password: ")

session = requests.Session()
session.auth = (username, password)


class PullRequest:

    amountPR = 0
    amountOpenPR = 0
    amountClosedPR = 0
    amountMergedPR = 0

    def __init__(self, user, repo, prnumber, state, creator, created, closed, merged):
        self.user = user
        self.repo = repo
        self.prnumber = prnumber
        self.state = state
        self.creator = creator
        self.created = parse_github_date(created)
        self.closed = parse_github_date(closed)
        self.merged = parse_github_date(merged)

        # statistic
        if state == "open":
            PullRequest.amountOpenPR += 1
        else:
            PullRequest.amountClosedPR += 1

        if self.merged != 'not':
            PullRequest.amountMergedPR += 1

        PullRequest.amountPR += 1

    def __str__(self):
        return "PR# {: >{w}}; " \
               "STATE - {: <6}; " \
               "CREATED - {}; " \
               "CLOSED - {}; " \
               "MERGED - {}; " \
               "CREATOR - {}."\
            .format(self.prnumber, self.state, self.created,
                    self.closed, self.merged, self.creator, w=len(str(PullRequest.amountPR)))


def getAllPullRequests(user, repo):
    temp_pulls = []
    # using for-loop because of paging of github-output (only 30 PR per time)
    for i in range(1, 100):
        url = 'https://api.github.com/repos/{user}/{repo}/pulls?page={i}&per_page=100&state=all'\
            .format(user=user, repo=repo, i=i)
        currentPage = (session.get(url)).json()
        if len(currentPage) == 0:
            break
        temp_pulls.extend(currentPage)

    pull_requests = []
    for iter in temp_pulls:
        pull_requests.append(PullRequest(user, repo, iter['number'], iter['state'],
                                         iter['user']['login'], iter['created_at'],
                                         iter['closed_at'], iter['merged_at']))

    return pull_requests


def parse_github_date(s):
    # 2019-06-24T10:17:09Z
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ') if s else 'not'
