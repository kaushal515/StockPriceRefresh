import re
import urllib.request

htmlfile = urllib.request.urlopen("http://finance.yahoo.com/q?s=GOOG")

htmltext = htmlfile.read().decode()

regex = '<span id="yfs_l84_goog">(.+?)</span>'

pattern = re.compile(regex)

price = re.findall(pattern,htmltext)

print (price)

