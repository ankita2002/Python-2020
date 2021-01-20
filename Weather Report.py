import requests
from bs4 import BeautifulSoup

class temperature(object):
    def __init__(self, place):
        self.place = place

    def __repr__(self):
        temp = self.weather() #temp-temperature
        return str(f"It's currently {temp} in {self.place}")

    def weather(self):
        url = f"https://www.google.com/search?&q=weather in {self.place}"
        req = requests.get(url)
        Report = BeautifulSoup(req.text, "html.parser")
        temp = Report.find("div", class_ ="BNeawe").text 
        return temp

if __name__ == "__main__":
    print(temperature("New York"))