from bs4 import BeautifulSoup as bs
import requests
import time
urls = []
with open('hotels.log','r') as f:
    for lines in f:
        l = lines.split()
        if (l[-1].endswith("#REVIEWS")):
            urls.append(l[-1])
f.close()
with open('ritesh.txt','w') as a:
    for links in urls:
        try:
            sourse = requests.get(links).text
            soup = bs(sourse,'lxml')
            for review_temp in soup.find_all('div', class_="hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"):
                review = review_temp.q.text
                print(review)
                print()
                a.write(review)
                a.write("\n")
        except:
            time.sleep(100)
a.close()