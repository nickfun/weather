from datetime import datetime
import math
import sys
import json

files = []

def getDate(sDate):
    oTime = datetime.strptime(sDate, "%Y-%m-%d_%H-%M.json")
    sNewDate = oTime.strftime("%c")
    return sNewDate

def toUnix(sDate):
    oTime = datetime.strptime(sDate, "%Y-%m-%d_%H-%M.json")
    dt0 = datetime(1970,1,1)
    return (oTime - dt0).total_seconds()

for arg in sys.argv:
    if arg[-5:] == ".json":
        files.append(arg)

firstfile = files.pop(0)
with open(firstfile, "r") as jsonin:
    data = json.loads(jsonin.read())
    print data[3]

for sDate in files:
    mydate = getDate(sDate)
    print "%s becomes %s unix: %d" % (sDate, mydate, toUnix(sDate))

print "Done"
