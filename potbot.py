from bs4 import BeautifulSoup
import csv
import requests

r = requests.get('http://potsherd.net/atlas/Ware/')
soup = BeautifulSoup(r.content, "html.parser")

# soup = BeautifulSoup(open("Africa.html"))

# final_link = soup.p.a
# final_link.decompose()

f = csv.writer(open("output.csv", "w"))
f.writerow([" ", "Link"])    # Write column headers as the first line

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')
        print (fulllink) #print in terminal to verify results
        f.writerow(["http://potsherd.net/atlas/", fulllink])    # Write column headers as the first line
