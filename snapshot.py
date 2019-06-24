import psutil
import time
import json

mb = 1024 * 1024


class Snapshot:
    """Common snapshot class"""

    snapshotCount = 0

    def __init__(self):
        Snapshot.snapshotCount += 1
        self.SNAPSHOT = Snapshot.snapshotCount
        self.TIMESTAMP = time.strftime("%Y.%m.%d %H:%M:%S")
        self.CPU_PERCENT = psutil.cpu_percent(interval=1, percpu=False)
        self.DISK_USED = psutil.disk_usage('/').used // mb
        self.DISK_TOTAL = psutil.disk_usage('/').total // mb
        self.VM_USED = psutil.virtual_memory().used // mb
        self.VM_TOTAL = psutil.virtual_memory().total // mb
        self.IO_READ = psutil.disk_io_counters().read_count
        self.IO_WRITE = psutil.disk_io_counters().write_count
        self.NTWK_SENT = psutil.net_io_counters().bytes_sent // mb
        self.NTWK_RECV = psutil.net_io_counters().bytes_recv // mb

    def __str__(self):
        return "SNAPSHOT %s: " \
               "%s: " \
               "CPU - %s %%; " \
               "Used/Total disk memory - %s/%s Mb; " \
               "Used/Total virtual memory - %s/%s Mb; " \
               "Read/Write count - %s/%s; " \
               "Sent/Received: %s/%s Mb.\n" \
               % (self.SNAPSHOT,
                   self.TIMESTAMP,
                   self.CPU_PERCENT,
                   str(self.DISK_USED), str(self.DISK_TOTAL),
                   str(self.VM_USED), str(self.VM_TOTAL),
                   str(self.IO_READ), str(self.IO_WRITE),
                   str(self.NTWK_SENT), str(self.NTWK_RECV))

    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
