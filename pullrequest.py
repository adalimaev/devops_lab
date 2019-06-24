import requests


user = 'alenaPy'
repo = 'devops_lab'
token = 'f63642c4677fd4ebf2f3b586133f623a614ce90b'


class PullRequest:

    amountPR = 0
    amountComments = 0

    def __init__(self, user, repo, prnumber, state, creator, created, closed):
        self.user = user
        self.repo = repo
        self.prnumber = prnumber
        self.state = state
        self.creator = creator
        self.created = created
        self.closed = closed
        self.comments = 0 # getComment(user, repo, prnumber)
        PullRequest.amountComments += self.comments
        PullRequest.amountPR += 1

    def __str__(self):
        return "PR# {}; STATE - {}; CREATOR - {}; CREATED - {}; CLOSED - {}; AmountComments - {}"\
            .format(self.prnumber, self.state, self.creator,
                    self.created, self.closed, self.comments)

def getComment(user, repo, pr_number):
    token = 'f63642c4677fd4ebf2f3b586133f623a614ce90b'
    comments = []
    # using for loop because of paging of github-output
    for i in range(1, 100):
        url = 'https://api.github.com/repos/{USER}/{REPO}/pulls/' \
              '{PRNUMBER}/comments?page={iter}&per_page=100&state=all'\
            .format(USER=user, REPO=repo, iter=i, PRNUMBER=pr_number)
        headers = {'Authorization': 'token %s' % token}
        current_comments = (requests.get(url, headers=headers)).json()
        if len(current_comments) == 0:
            return len(comments)
        comments.extend(current_comments)


def getAllPR(user, repo):
    PRStemp = []
    # using for loop because of paging of github-output
    for i in range(1, 100):
        url = 'https://api.github.com/repos/{user}/{repo}/pulls?page={i}&per_page=100&state=all'\
            .format(user=user, repo=repo, i=i)
        headers = {'Authorization': 'token %s' % token}
        currentPage = (requests.get(url, headers=headers)).json()
        if len(currentPage) == 0:
            break
        PRStemp.extend(currentPage)
    PRS = []
    for iter in PRStemp:
        # print("Number: {}, STATE: {}, CREATED: {}, WHOm: {}, CLOSED: {}"
        #       .format(iter['number'], iter['state'], iter['created_at'],
        #       iter['user']['login'], iter['closed_at']))
        PRS.append(PullRequest(user, repo, iter['number'],
                               iter['state'], iter['user']['login'],
                               iter['created_at'], iter['closed_at']))

    # print(PRS[0])
    return PRS
