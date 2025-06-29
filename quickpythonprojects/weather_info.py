import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

#create an object of ToastNotifier class
n = ToastNotifier()

#Define a function for getting data from the given url
def getdata(url):
    r = requests.get(url)
    return r.text

#Now pass the URL into the getdata function and Convert that data into HTML code.
htmldata = getdata("https://weather.com/tr-TR/weather/today/l/7c266341bb68352ff0a61698c4361d0fbbf3fd7de795907a1a91bd885e7a9f36")


soup = BeautifulSoup(htmldata, 'html.parser')

print(soup.prettify())


#find the required details and filter them
current_temp = soup.find_all("span", 
                             class_="CurrentConditions--tempValue--MHmYY")
                             

chances_rain = soup.find_all("span", 
                             class_="CurrentConditions--precipValue--2aJSf")
temp = (str(current_temp))

temp_rain = str(chances_rain)

result = "current_temp " + temp[128:-9] + "  in itü ayazağa" + "\n" +temp_rain[131:-14]





n.show_toast("Weather update", result, duration = 10)
time.sleep(15)