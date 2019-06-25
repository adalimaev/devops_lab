
#### Output task 1

This Python script get pull request information of chosen user's perository.


#### Usage and Options

usage: `prstats.py [-h] [-s] [-r] [-p] [-d] [-c] [-a AFTER] user repo`

positional arguments:  
  `user`                  set current user  
  `repo`                  set repository name

optional arguments:
  `-h, --help`               show this help message and exit  
  `-s, --state`              state of PR  
  `-r, --rate`               show basic statistic open/closed/merged/all rate  
  `-p, --pretty`             pretty format of dates (Names of days, weeks), require -d option  
  `-d, --dates`              show creation/closing dates  
  `-c, --creator`            show who open PR  
  `-a AFTER, --after AFTER`  show PRs which opened after date DD.MM.YYYY(including)  

