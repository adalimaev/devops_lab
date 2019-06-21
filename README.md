### watcher


#### Description

This Python app gets common system information every given time interval and writes to the log file.  
Default setting can be changed in "watcher/watcher_config.py" file.


#### Installation

Wheel-package is in `devops_lab/` directory.  
To install use

`pip install devops_lab/watcher-0.1-py3-none-any.whl`

To verify installation, enter in python interactive console (from any location except `devops_lab` directory) and type `import watcher`. Then enter `watcher.__path__` and check that package is in `.../site-packages` directory.


#### Running

`../site-packages]$ python watcher`

To run application, from `.../site-packages` location in console enter `python watcher`. The application will run with default setting (see below). To run app with other setting you can use additional arguments or you can change watcher_config file.


#### Settings

You can use optional parameters to run this application. There are the follow parameters:

  `-h, --help`  show help message and exit;
  
  `-i [I]`      Set update interval (in seconds). Default = 5 seconds;

  `-f [F]`      Set output format txt|json. Default - "txt";

  `-t [T]`      Set program work time. Default = 30 seconds.

When you are running without argument, application use default value (see above) of missed parameter.


#### Output examples

1. `../site-packages]$ python watcher -i 2 -f json -t 6`

`/tmp/watcher.log:`

`{
    "SNAPSHOT": 1,
    "TIMESTAMP": "2019.06.21 20:45:08",
    "CPU_PERCENT": 7.8,
    "DISK_USED": 187399,
    "DISK_TOTAL": 669422,
    "VM_USED": 4584,
    "VM_TOTAL": 15776,
    "IO_READ": 322994,
    "IO_WRITE": 2132248,
    "NTWK_SENT": 192,
    "NTWK_RECV": 2535
}`

2. `../site-packages]$ python watcher -i 3 -f txt -t 10`

`/tmp/watcher.log:`

`SNAPSHOT 1: 2019.06.21 20:46:38: CPU - 7.8 %; Used/Total disk memory - 187399/669422 Mb; Used/Total virtual memory - 4589/15776 Mb; Read/Write count - 322994/2133184; Sent/Received: 192/2535 Mb.`  
`SNAPSHOT 2: 2019.06.21 20:46:41: CPU - 7.5 %; Used/Total disk memory - 187399/669422 Mb; Used/Total virtual memory - 4589/15776 Mb; Read/Write count - 322994/2133186; Sent/Received: 192/2535 Mb.`  
`SNAPSHOT 3: 2019.06.21 20:46:44: CPU - 7.7 %; Used/Total disk memory - 187399/669422 Mb; Used/Total virtual memory - 4588/15776 Mb; Read/Write count - 322994/2133196; Sent/Received: 192/2535 Mb.`  
`SNAPSHOT 4: 2019.06.21 20:46:47: CPU - 7.8 %; Used/Total disk memory - 187399/669422 Mb; Used/Total virtual memory - 4589/15776 Mb; Read/Write count - 322994/2133222; Sent/Received: 192/2535 Mb.`  
