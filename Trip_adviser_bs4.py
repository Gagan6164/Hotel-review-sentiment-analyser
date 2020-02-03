from bs4 import BeautifulSoup as bs
import requests
import time
urls = []
with open('hotels.txt','r') as f:
    for lines in f:
        l = lines.split()
        if (l[-1].endswith("#REVIEWS")):
            urls.append(l[-1])
f.close()
with open('ritesh.txt','w') as a:
    for links in urls:
        print("Processing url :{}".format(links))
        try:
            sourse = requests.get(links).text
            soup = bs(sourse,'lxml')
            total_reviews = soup.find('span', class_="hotels-community-content-common-TabAboveHeader__tabCount--26Tct").text
            total_reviews = int(total_reviews)
            for pages in range(0,total_reviews,5):
                if (pages !=0 ):
                    s = "-or{}-".format(pages)
                    link = links.split("-")
                    new_link = link[0]+"-".join(i for i in link[1:3])+ s + "-".join(i for i in link[4:])
                    sourse = requests.get(new_link).text
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
            print("Connection error Retrying in 10 sec...")
            time.sleep(100)
a.close()


def get_hotal_review_urls(hotel_url):
    sourse = requests.get(hotel_url).content
    soup = bs(sourse,'lxml')
    total_review_pages = soup.find('a', class_="last").text
    total_review_pages = int(total_reviews)
    hotal_review_links =  []
    for pages in range(0,total_review_pages):
        if (pages !=0 ):
            s = "-or{}-".format(pages*5)
            link = links.split("-")
            new_link = link[0]+"-".join(i for i in link[1:3])+ s + "-".join(i for i in link[4:])
        hotal_review_links.append(new_link)
    return new_link