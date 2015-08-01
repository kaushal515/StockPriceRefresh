import re
import urllib.request

symbol = input("Please enter stock symbol :  ")

htmlfile = urllib.request.urlopen('http://finance.yahoo.com/q?s='+symbol+'&ql=0')

htmltext = htmlfile.read().decode()



#regex = '<span id="yfs_l84_indosolar.ns">(.+?)</span>'

regex = '<span id="yfs_l84_'+symbol+'">(.+?)</span>'

pattern = re.compile(regex)

price = re.findall(pattern,htmltext)

print (price)

