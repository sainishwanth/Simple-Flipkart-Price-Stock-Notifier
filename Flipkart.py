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

class item():  #Class which contains methods and attributes of the product
    def __init__(self,URL,page,soup):
        self.page = page
        self.URL = URL
        self.soup = soup
    
    def price(self): #Method to retrieve the price of the item
        self.page = requests.get(URL, headers = header)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        try:
            price = self.soup.find("div", class_ = "_30jeq3 _16Jk6d").get_text().strip()
            price = price.replace(',','')
            return int(price[1:])
        except:
            pass
    
    def stock(self):  #Method to check if the item is in stock
        self.page = requests.get(URL, headers = header)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        try:
            stock = self.soup.find("div", class_ = "_16FRp0").get_text().strip()
            return stock
        except:
            return None
        
    @staticmethod
    def music(path1):  #Method to Play Music. (Not an attribute of Product but welp)
        try:
            path.exists(path1 + '/alarm.wav')    #Unix Convention of file management
            path1 = path1 + '/alarm.wav'
        except:
            path.exists(path1 + '\alarm.wav')    #Windows Convention of file Managament
            path1 = path1 + '\alarm.wav'      
        webbrowser.open(URL)                     #Opening the Product Page 
        playsound(path1)                         #Playing the "Music" i.e Alarm when triggered
            

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
            
            if price_limit >= product.price(): #Loop that keeps checking for if the price has fallen below the price set by the user
                product.music(path1)
            else:
                time.sleep(10)
                print("Running..")
                continue
            break
    elif inpt == 2:                            #Loop for checking if the item is in stock
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
