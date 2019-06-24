#!/usr/bin/env python

# import configparser
import snapshot as sh
import time
import argparse
import watcher_config as wc

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
logFile = wc.config['logFile']
outputType = args.f if args.f else wc.config['outputType']
interval = int(args.i if args.i else wc.config['interval'])
workTime = int(args.t if args.t else wc.config['workTime'])

# clear log file
f = open(logFile, "w")
f.write("")
f.close()

startTime = endTime = time.time()
while endTime - startTime < workTime:
    currentSnapshot = sh.Snapshot()
    if outputType == "json":
        # print(currentSnapshot.tojson())
        f = open(logFile, "a")
        f.write(currentSnapshot.tojson())
        f.close()
    else:
        # print(currentSnapshot)
        f = open(logFile, "a")
        f.write(str(currentSnapshot))
        f.close()

    time.sleep(interval - 1)
    endTime = time.time()
