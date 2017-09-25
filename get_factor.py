import json
from urllib2 import urlopen
from bs4 import BeautifulSoup
def factor(n):
    url = "http://factordb.com/index.php?query="+str(n)
    f = urlopen(url)
    content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    temps = soup.find_all("font", attrs={'color': '#000000'})
    s = ' x '.join(temp.get_text() for temp in temps)
    return s

n = int(raw_input("nhap so: "))
print "phan tich thanh: " + factor(n)