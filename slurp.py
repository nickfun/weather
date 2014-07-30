# download the public json file
#
# Nick F 
# Tue Jul 29 19:25:21 PDT 2014

import urllib
import datetime

timeNow = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
localFile = timeNow + ".json"
urllib.urlretrieve("http://www.weatherlink.com/mapstations.json", localFile);

with open("/home/nick/weather/log.txt", "a") as myfile:
    myfile.write(timeNow + " - Downloaded json file\n")

print "Done!"

