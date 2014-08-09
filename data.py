from datetime import datetime
import riak
import math
import sys
import json

files = []
rc = riak.RiakClient(pb_port=8087, protocol='pbc')

def filenameToDate(sDate):
    return datetime.strptime(sDate, "%Y-%m-%d_%H-%M.json")


def filenameToUnix(sDate):
    oTime = filenameToDate(sDate)
    dt0 = datetime(1970,1,1)
    return (oTime - dt0).total_seconds()

# Of the filenames passed to us, keep the ones that end in .json
for arg in sys.argv:
    if arg[-5:] == ".json":
        files.append(arg)

# For all those files, read the files and insert the data into the database
for sFile in files:
    oDate = filenameToDate(sFile)
    iDate = filenameToUnix(sFile)
    with open(sFile, "r") as inputFile:
        print "Begin: %s" % sFile
        data = json.load(inputFile)
        for station in data:
            bucket = rc.bucket(station['DID'])
            key = bucket.new(iDate, data=station)
            key.store()
            print "store: %s" % station['uname']
        print "Done: %s" % sFile

print "Done: ALL"
