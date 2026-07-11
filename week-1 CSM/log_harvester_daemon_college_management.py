"""
College Management System - log_harvester_daemon.py
"""
import socket,threading,re,struct,os,time
from collections import defaultdict

HOST="127.0.0.1"
PARTITION_DIR="partitions"
BRANCHES=[("BCA",9001),("ComputerScience",9002),("Accounts",9003)]

LOG_PATTERN=re.compile(
r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*\|\s*"
r"(?P<level>INFO|WARNING|ERROR|DEBUG)\s*\|\s*"
r"(?P<department>[\w\-]+)\s*\|\s*"
r"(?P<event>.+)$")

LEVEL_CODE={"DEBUG":0,"INFO":1,"WARNING":2,"ERROR":3}
files={}
locks=defaultdict(threading.Lock)
stats=defaultdict(int)
stats_lock=threading.Lock()

def partfile(dep,level):
    os.makedirs(PARTITION_DIR,exist_ok=True)
    k=(dep,level)
    if k not in files:
        files[k]=open(os.path.join(PARTITION_DIR,f"{dep}_{level}.bin"),"ab")
    return files[k]

def encode(ts,level,dep,event):
    tb=ts.encode().ljust(19,b" ")[:19]
    db=dep.encode()
    eb=event.encode()
    rec=struct.pack("!19sBH",tb,LEVEL_CODE[level],len(db))+db+struct.pack("!H",len(eb))+eb
    return struct.pack("!I",len(rec))+rec

def process(line,branch):
    m=LOG_PATTERN.match(line)
    if not m:
        with stats_lock: stats[(branch,"REJECTED")]+=1
        return
    data=encode(m["timestamp"],m["level"],m["department"],m["event"])
    f=partfile(m["department"],m["level"])
    with locks[(m["department"],m["level"])]:
        f.write(data); f.flush()
    with stats_lock: stats[(branch,m["level"])]+=1

def worker(name,port):
    s=socket.socket()
    s.connect((HOST,port))
    print(f"{name} connected")
    buf=b""
    try:
        while True:
            c=s.recv(4096)
            if not c: break
            buf+=c
            while b"\n" in buf:
                line,buf=buf.split(b"\n",1)
                try: process(line.decode().strip(),name)
                except UnicodeDecodeError: pass
    finally:
        s.close()

def dashboard():
    while True:
        time.sleep(3)
        with stats_lock:
            if stats:
                print("\n---Stats---")
                for k,v in sorted(stats.items()):
                    print(k,v)

if __name__=="__main__":
    for n,p in BRANCHES:
        threading.Thread(target=worker,args=(n,p),daemon=True).start()
    threading.Thread(target=dashboard,daemon=True).start()
    print("College Management Harvester Running")
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        for f in files.values(): f.close()
