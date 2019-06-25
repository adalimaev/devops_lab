#!/usr/bin/env python

import subprocess
import sys
import site
import json
import yaml

data = {}

data.update({'Current': {}})

#  1
cmd = 'python -V'
proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output = str(proc.stdout.read())[2:-3].split()
data['Current'].update({'VERSION': output[1]})

#  2
data['Current'].update({'ENV_NAME': str(sys.prefix).split('/')[-1]})

#  3
data['Current'].update({'EXEC_LOCATION': sys.prefix})

#  4
cmd = ['pip', '-V']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
output = str(proc.stdout.read())[2:-3].split()
data['Current'].update({'PIP_LOCATION': output[3]})

#  5
data['Current'].update({'PYTHONPATH': sys.path})

#  6
data['Current'].update({'INSTALLED_PCKGS': {}})
cmd = ['pip', 'freeze']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
packages = str(proc.stdout.read())[2:-3]
if len(packages) != 0:
    for i in packages.split('\\n'):
        name, version = i.split('==')
        data['Current']['INSTALLED_PCKGS'].update({name: version})

#  7
data['Current'].update({'SITE_PKGS_LOCATION': site.getsitepackages()})

with open('output.json', 'w') as f_json:
    json.dump(data, f_json, indent=4)

with open('output.yml', 'w') as f_yml:
    yaml.dump(data, f_yml)
