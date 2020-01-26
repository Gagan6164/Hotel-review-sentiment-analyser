from bs4 import BeautifulSoup as bs
import requests

sourse = requests.get("https://www.tripadvisor.in/Hotel_Review-g616028-d619324-Reviews-Haveli_Hari_Ganga_by_Leisure_Hotels-Haridwar_Haridwar_District_Uttarakhand.html#REVIEWS").text

soup = bs(sourse,'lxml')
for review_temp in soup.find_all('div', class_="hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"):
    review = review_temp.q.text
    print(review)
    print()
