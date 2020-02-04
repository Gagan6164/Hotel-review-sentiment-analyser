from bs4 import BeautifulSoup as bs
import requests
import time

"""


                    sourse = requests.get(new_link).text
                    soup = bs(sourse,'lxml')
                for review_temp in soup.find_all('div', class_="hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"):
                    review = review_temp.q.text
                    rate_5 = review_temp.find_all('span',class_="ui_bubble_rating bubble_50")
                    if(rate_5!=[]):
                        rating=5
                    rate_4 = review_temp.find_all('span',class_="ui_bubble_rating bubble_40")
                    if(rate_4!=[]):
                        rating=4
                    rate_3 = review_temp.find_all('span',class_="ui_bubble_rating bubble_30")
                    if(rate_3!=[]):
                        rating=3
                    rate_2 = review_temp.find_all('span',class_="ui_bubble_rating bubble_20")
                    if(rate_2!=[]):
                        rating=2
                    rate_1 = review_temp.find_all('span',class_="ui_bubble_rating bubble_10")
                    if(rate_1!=[]):
                        rating=1
                    print(review)
                    print()
                    re = str(review)+"    rating = "+str(rating)
                    a.write(re)
                    a.write("\n")
        except:
            print("Connection error Retrying in 10 sec...")
            time.sleep(100)
a.close()
"""

def get_hotal_review_urls(hotel_url):
    sourse = requests.get(hotel_url).content
    soup = bs(sourse,'lxml')
    total_review_pages = soup.find_all('a', class_="pageNum ")
    try:
        total_review_pages = int(total_review_pages[-1].contents[0])
    except:
        total_review_pages = 1
    hotal_review_links =  []
    for pages in range(0,total_review_pages):
        new_link = hotel_url
        if (pages ==0 ):
            s = "-or{}-".format(pages*5)
            link = hotel_url.split("-")
            new_link = "-".join(i for i in link[0:4])+ s + "-".join(i for i in link[4:])
        hotal_review_links.append(new_link)
    return hotal_review_links


def get_hotel_url(file):
    hotel_urls = []
    with open(file,'r') as f:
        for lines in f:
            l = lines.split()
            if (l[-1].endswith("html")):
                hotel_urls.append(str(l[-1]+"#REVIEWS"))
    f.close()
    return hotel_urls


def get_reviews(hotel_review_url):
    sourse = requests.get(hotel_review_url).text
    soup = bs(sourse,'lxml')
    for review_temp in soup.find_all('div', class_="hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"):
        review = review_temp.q.text
        rate_5 = review_temp.find_all('span',class_="ui_bubble_rating bubble_50")
        if(rate_5!=[]):
            user_given_rating=5
        rate_4 = review_temp.find_all('span',class_="ui_bubble_rating bubble_40")
            if(rate_4!=[]):
                user_given_rating=4
        rate_3 = review_temp.find_all('span',class_="ui_bubble_rating bubble_30")
            if(rate_3!=[]):
                user_given_rating=3
        rate_2 = review_temp.find_all('span',class_="ui_bubble_rating bubble_20")
            if(rate_2!=[]):
                user_given_rating=2
        rate_1 = review_temp.find_all('span',class_="ui_bubble_rating bubble_10")
            if(rate_1!=[]):
                user_given_rating=1
        print(review)
        print()
        re = str(review)+"    rating = "+str(user_given_rating)


if __name__=='__main__':
    print("Started reading hotel urls file")
    hotel_urls = get_hotel_url('hotels.txt')
    print("Done reading hotel urls")
    print("-"*10)
    for hotel_url in hotel_urls:
        print("started getting hotel review urls links")
        print(hotel_url)
        hotel_review_url = get_hotal_review_urls(hotel_url)
