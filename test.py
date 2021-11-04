import os
from pathlib import Path

source = "cc.txt"
dest = "hi.txt"


curpath = Path(source)
bytesToSend = None
with open(curpath, 'rb') as f:
    filesize=int(os.path.getsize(curpath))
    bytesToSend = f.read(filesize)
    print(type(bytesToSend))
    
with open(dest, "wb") as f:
    f.write(bytesToSend)