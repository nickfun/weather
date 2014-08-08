import math
import sys
import json

files = []

for arg in sys.argv:
    if arg[-5:] == ".json":
        files.append(arg)

firstfile = files.pop(0)
with open(firstfile, "r") as jsonin:
    data = json.loads(jsonin.read())
    print data[0]
    print data[3]

print "Done"
