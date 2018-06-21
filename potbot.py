from bs4 import BeautifulSoup
import csv
import requests
import re

r = requests.get('http://potsherd.net/atlas/Ware/ALL')
soup = BeautifulSoup(r.content, "html5lib")

f = csv.writer(open("output.csv", "w"))

trs = soup.find_all('tr')
for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')
        print (fulllink) #print in terminal to verify results
        f.writerow(["http://potsherd.net/atlas/" + fulllink])    # Write column headers as the first line
