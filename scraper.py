from bs4 import BeautifulSoup
import urllib.request
import time
for i in range(0,150):
    url = 'https://www.chiefdelphi.com/forums/portal.php'
    r = urllib.request.urlopen(url).read()
    try:
        soup = BeautifulSoup(r, "lxml")
    except:
        soup = BeautifulSoup(r, "html.parser")
        quote = soup.find("td", class_="spotlight").contents

    cleanedQuote=quote[0]

    print(cleanedQuote)
    time.sleep(.25)
