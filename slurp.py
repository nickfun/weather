# download the public json file
#
# Nick F 
# Tue Jul 29 19:25:21 PDT 2014

import urllib
import datetime

logFile = "/home/nick/weather/log.txt"
timeNow = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
localFile = "/home/nick/weather/" + timeNow + ".json"
print "Begin file load"
urllib.urlretrieve("http://www.weatherlink.com/mapstations.json", localFile);
print "Write to log file"
with open(logFile, "a") as myfile:
    myfile.write(timeNow + " - Downloaded json file\n")

print "Done!"

