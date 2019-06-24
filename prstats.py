#!/usr/bin/env python

import pullrequest
import argparse
from datetime import datetime
import calendar

parser = argparse.ArgumentParser()
parser.add_argument("user", help="set current user")
parser.add_argument("repo", help="set repository name")
parser.add_argument("-s", "--state", help="state of PR", action="store_true")
parser.add_argument("-r", "--rate", help="show basic statistic open/closed/merged/all rate",
                    action="store_true")
parser.add_argument("-p", "--pretty", help="pretty format of dates (Names of days, weeks), "
                                           "require -d option", action="store_true")
parser.add_argument("-d", "--dates", help="show creation/closing dates", action="store_true")
parser.add_argument("-c", "--creator", help="show who open PR", action="store_true")
parser.add_argument("-a", "--after", help="show PRs which opened after date DD.MM.YYYY(including)")
args = parser.parse_args()

user = args.user
repo = args.repo


def isPullRequestAfterArgsDate(iter_date):
    if args.after:
        return datetime.strptime(args.after, '%d.%m.%Y') < iter_date
    else:
        return True


def getPrettyDate(dt, s):
    line = ""
    day = calendar.day_name[calendar.weekday(dt.year, dt.month, dt.day)]
    line += "%s on %s " % (s, str(day))
    line += "%sth %s %s; " % (str(dt.day), str(calendar.month_name[dt.month]), str(dt.year))
    return line


PR = pullrequest.getAllPullRequests(user, repo)


print("{user}'s \"{repo}\" repository statistics:".format(user=user, repo=repo))

if not args.state and not args.dates and not args.creator and not args.after:
    print("There are %d pull requests. "
          "Please, run script with options to show information." % len(PR))
else:
    for iter in PR:
        if isPullRequestAfterArgsDate(iter.created):
            line = ""
            line += "PR# {: >{w}}; "\
                .format(iter.prnumber, w=len(str(pullrequest.PullRequest.amountPR)))

            #  -s (--state) option
            if args.state:
                line += "state - {: <6}; ".format(iter.state)

            #  -d (--dates) prefix
            if args.dates:
                line += "PR "
                #  -p (--pretty) option
                if args.pretty:
                    line += getPrettyDate(iter.created, "created")
                    if iter.closed != 'not':
                        line += getPrettyDate(iter.closed, "closed")
                else:
                    line += "created - {}; closed - {}; merged - {}; "\
                        .format(iter.created, iter.closed, iter.merged)

            #  -c (--creator) option
            if args.creator:
                line += "creator - %s; " % iter.creator

            print(line[:-2])

#  -r (--rate) option
if args.rate:
    print("Amount of open/closed/merged/all PRs: {}/{}/{}/{}".
          format(pullrequest.PullRequest.amountOpenPR, pullrequest.PullRequest.amountClosedPR,
                 pullrequest.PullRequest.amountMergedPR, pullrequest.PullRequest.amountPR))
