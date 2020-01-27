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
                rate_5 = review_temp.find_all('span',class_="ui_bubble_rating bubble_50")
                if(rate_5!=[]):
                    raat=5
                rate_4 = review_temp.find_all('span',class_="ui_bubble_rating bubble_40")
                if(rate_4!=[]):
                    raat=4
                rate_3 = review_temp.find_all('span',class_="ui_bubble_rating bubble_30")
                if(rate_3!=[]):
                    raat=3
                rate_2 = review_temp.find_all('span',class_="ui_bubble_rating bubble_20")
                if(rate_2!=[]):
                    raat=2
                rate_1 = review_temp.find_all('span',class_="ui_bubble_rating bubble_10")
                if(rate_1!=[]):
                    raat=1
                
                print(review)
                print()
                re = str(review)+"    rating = "+str(raat)
                a.write(re)
                a.write("\n")
        except:
            time.sleep(100)
a.close()