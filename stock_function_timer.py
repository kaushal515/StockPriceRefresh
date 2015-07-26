import re
import urllib.request
import time

def get_stock_price():
 i = 0  
 while i < 3 :

  i = i+1
   
  htmlfile = urllib.request.urlopen("http://finance.yahoo.com/q?s=GOOG")

  htmltext = htmlfile.read().decode()

  regex = '<span id="yfs_l84_goog">(.+?)</span>'

  pattern = re.compile(regex)

  price = re.findall(pattern,htmltext)

  print (price)

  time.sleep(30)

  
