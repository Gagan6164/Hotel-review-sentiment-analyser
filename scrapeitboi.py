from bs4 import BeautifulSoup as bs
import requests as req
import re
import time
import xlwt 
from xlwt import Workbook 
HotelURLS = []
TripAdvisorURLS = ["https://www.tripadvisor.in/Hotels-g616028-Haridwar_Haridwar_District_Uttarakhand-Hotels.html"]
for i in range(1,11):
    TripAdvisorURLS.append("https://www.tripadvisor.in/Hotels-g616028-oa"+str(30*i)+"-Haridwar_Haridwar_District_Uttarakhand-Hotels.html")
for i in TripAdvisorURLS:
    res = req.get(i)
    if(res.status_code >= 400):
        print("Error : %s" % res.status_code)
        continue
    pagesoup = bs(res.text, 'html.parser')
    AllLinks = pagesoup.findAll('div',class_ = "listing_title")
    for link in AllLinks:
        HotelURLS.append("https://www.tripadvisor.in"+link.find('a',attrs = {'href': re.compile("^/")}).get('href'))
        break
    break
del TripAdvisorURLS    
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
style = xlwt.easyxf('font: bold 1')
sheet1.write(0,0,'SERIAL NO.',style)
sheet1.write(0,1,'NAME',style)
sheet1.write(0,2,'RATING',style)
sheet1.write(0,3,'HEADING',style)
sheet1.write(0,4,'REVIEW',style)
SrNo=0
for i in HotelURLS:
    res = req.get(i)
    if(res.status_code >= 400):
        print("Error : %s" % res.status_code)
        continue
    pagesoup = bs(res.text, 'html.parser')
    number = int(int(pagesoup.findAll('span',class_="hotels-community-content-common-TabAboveHeader__tabCount--26Tct")[0].text)*0.2)
    RevurlAllPage = [i+"#REVIEWS"]
    for j in range(1,number):
        RevurlAllPage.append(i[:65]+"-or"+str(5*i)+i[65:]+"#REVIEWS")
    for l in RevurlAllPage:
        res = req.get(l)
        if(res.status_code>=400):
            print("Error : %s"%res.status_code)
            continue
        pagesoup = bs(res.text, 'html.parser')
        name = []
        rating = []
        heading = []
        body = []
        person = pagesoup.findAll('div',class_="social-member-event-MemberEventOnObjectBlock__event_type--3njyv")
        for m in person:
            name.append(m.find('a',attrs={'href': re.compile("^/")}).get('href'))
        person = pagesoup.findAll('div',class_="location-review-review-list-parts-RatingLine__bubbles--GcJvM")
        for m in person:
            rating.append(m.find('span',attrs={'class': re.compile("^")}).get('class'))
        person = pagesoup.findAll('a',class_="location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT")
        for m in person:
            heading.append(m.find('span').text)
        person = pagesoup.findAll('q',class_="location-review-review-list-parts-ExpandableReview__reviewText--gOmRC")
        for m in person:
            body.append(m.find('span').text)
        for m in range(5):
            SrNo += 1
            sheet1.write(SrNo,0,SrNo)
            sheet1.write(SrNo,1,name[m])
            sheet1.write(SrNo,2,int(rating[m][1][-2:-1]))
            sheet1.write(SrNo,3,heading[m])
            sheet1.write(SrNo,4,body[m])
        break
    break
    time.sleep(1)
wb.save('reviews.xls')
