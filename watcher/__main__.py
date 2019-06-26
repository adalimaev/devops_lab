#!/usr/bin/env python

# import configparser
from watcher import snapshot
import time
import argparse
from watcher import watcher_config

# parsing arguments
arguments = argparse.ArgumentParser(description='Gets common system information every given time '
                                                'interval and writes to the file. '
                                                'Default setting can be changed '
                                                'in "watcher_config".')
arguments.add_argument('-i', nargs='?', help='Set update interval (in seconds). '
                                             'Default = 5 seconds')
arguments.add_argument('-f', nargs='?', help='Set output format txt|json. Default - "txt"')
arguments.add_argument('-t', nargs='?', help='Set program work time. Default = 30 seconds')
args = arguments.parse_args()

# parsing config file
logFile = watcher_config.config['logFile']
outputType = args.f if args.f else watcher_config.config['outputType']
interval = int(args.i if args.i else watcher_config.config['interval'])
workTime = int(args.t if args.t else watcher_config.config['workTime'])

# clear log file
with open(logFile, "w") as f:
    f.write("")

startTime = endTime = time.time()
while endTime - startTime < workTime:
    currentSnapshot = snapshot.Snapshot()
    if outputType == "json":
        with open(logFile, "a") as f:
            f.write(currentSnapshot.tojson())
    else:
        with open(logFile, "a") as f:
            f.write(str(currentSnapshot))

    time.sleep(interval)
    endTime = time.time()
