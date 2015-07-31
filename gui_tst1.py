from tkinter import *
from tkinter.ttk import *
import re
import urllib.request
import time

def get_stock_price():
 i = 0  
 while i < 3 :

  i = i+1
   
  htmlfile = urllib.request.urlopen("http://finance.yahoo.com/q?s=indosolar.ns&ql=0")

  htmltext = htmlfile.read().decode()

  regex = '<span id="yfs_l84_indosolar.ns">(.+?)</span>'

  pattern = re.compile(regex)

  price = re.findall(pattern,htmltext)

  print (price)

  time.sleep(5)

root = Tk()
root.title('Twitter Stream')

#mainframe = tkinter.ttk.Frame(root)
root.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

symbol = StringVar()

symbol_entry = Entry(root, width=7, textvariable=symbol)
symbol_entry.grid()

symbol_label=Label(root, text="Stock Symbol").grid()

stock_button=Button(root, text="Get stock price", command=get_stock_price).grid()

root.mainloop()

