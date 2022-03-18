import webbrowser
import time
import requests
import os
from os import path
from bs4 import BeautifulSoup
from playsound import playsound

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
path1 = os.getcwd()
URL = input("Enter the URL: ")

class item():
    def __init__(self,URL,page,soup):
        self.page = page
        self.URL = URL
        self.soup = soup
    
    def price(self):
        self.page = requests.get(URL, headers = header)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        try:
            price = self.soup.find("div", class_ = "_30jeq3 _16Jk6d").get_text().strip()
            price = price.replace(',','')
            return int(price[1:])
        except:
            pass
    
    def stock(self):
        self.page = requests.get(URL, headers = header)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        try:
            stock = self.soup.find("div", class_ = "_16FRp0").get_text().strip()
            return stock
        except:
            return None
        
    @staticmethod
    def music(path1):
        try:
            path.exists(path1 + '/alarm.wav')
            path1 = path1 + '/alarm.wav'
        except:
            path.exists(path1 + '\alarm.wav')
            path1 = path1 + '\alarm.wav'
        webbrowser.open(URL)
        playsound(path1)
            

def main():
    while True:
        page = requests.get(URL, headers = header)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            title = soup.find("span", class_ = "B_NuCI").get_text().strip()
            break
        except:
            pass
    print("\n"+title+"\n")
    product = item(URL,page,soup)
    print(f"Price - {product.price()}")
    inpt = int(input("1.Price Notifier\n2.Stock Notifier: "))
    if inpt == 1:
        price_limit = int(input("Enter the Price Threshold: "))
        while True:
            
            if price_limit >= product.price():
                product.music(path1)
            else:
                time.sleep(10)
                print("Running..")
                continue
            break
    elif inpt == 2:
        while True:
            if product.stock() is  None:
                product.music(path1)
            else:
                time.sleep(10)
                print("Running..")
                continue
            break

if __name__ == "__main__":
    main()
