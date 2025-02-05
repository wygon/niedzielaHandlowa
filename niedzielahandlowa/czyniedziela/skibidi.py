import requests
from bs4 import BeautifulSoup
import datetime
months = {
        "stycznia" : 1,
        "lutego" : 2,
        "marca" : 3,
        "kwietnia" : 4,
        "maja" : 5,
        "czerwca" : 6,
        "lipca" : 7,
        "sierpnia" : 8,
        "września" : 9,
        "października" : 10,
        "listopada" : 11,
        "grudnia" : 12
    }
def getSoupList():
    url = "https://www.aldi.pl/informacje-dla-klienta/niedziele-handlowe-2025.html"
    # print(now)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    soupListDiv = soup.find('div', {"class": "rte"})
    soupList = soupListDiv.find_all('li')
    soupTradeSundayList = []
    for item in soupList:
        item = item.text.replace("niedziela handlowa ", "")
        item = item.replace("\xa0", " ")
        soupTradeSundayList.append(item)
    return(soupTradeSundayList)

def dateValidation(gsl):
    tradeSundayList = []

    for date in gsl:
        parts = date.split()
        day = int(parts[0])
        month = months[parts[1]]
        year = int(parts[2])
        tradeSundayList.append(f"{year:04d}-{month:02d}-{day:02d}")
    return tradeSundayList

def isTradingSunday():
    gsl = getSoupList()
    now = datetime.date.today()
    tradeSundayList = dateValidation(gsl)
    
    return now.strftime("%Y-%m-%d") in tradeSundayList
        
print(isTradingSunday())