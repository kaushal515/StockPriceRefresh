# StockPriceRefresh

Web scraping finance.yahoo.com to get spot price of a stock

There are two files 

one,  which only makes an url request to finance.yahoo.com and fetches the spot price

second, where I have created a function get_stock_price which makes an url request to finance.yahoo.com and sleeps for 30 seconds before it makes another url request. 
* You can specify your own time depending on how frequently you want to get the stock price. 
* change  while i < 3 to while true if you want to keep scraping. 
* currently not taking inputs from user

===================================================================

Steps : 

1 : go to finance.yahoo.com and search for stock you want ( in this example google )

2 : get the stock symbol ( GOOG in this example )

3 : replace the stock symbol in the code , lets say Apple ( stock symbol AAPL )

change htmlfile = urllib.request.urlopen("http://finance.yahoo.com/q?s=AAPL"3

and

regex = '<span id="yfs_l84_aapl">(.+?)</span>
	
	
===================================================================


Setup : 

>>> 
>>> get_stock_price()

====================================================================

Modules required : 

urllib

re

====================================================================

Credits : 

https://www.youtube.com/watch?v=f2h41uEi0xU

====================================================================


