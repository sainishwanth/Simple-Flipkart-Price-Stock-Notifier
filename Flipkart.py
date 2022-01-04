import webbrowser
import time
import requests
import os
from bs4 import  BeautifulSoup
from playsound import PlaysoundException, playsound

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

URL = input("Enter the URL: ")

def price(page, soup):
    page = requests.get(URL, headers = header)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        price = soup.find("div", class_ = "_30jeq3 _16Jk6d").get_text().strip()
        price = price.replace(',','')
        return int(price[1:])
    except:
        price(page,soup)

def stock(page,soup):
    page = requests.get(URL, headers = header)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        stock = soup.find("div", class_ = "_16FRp0").get_text().strip()
        return stock
    except:
        return None

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
    inpt = int(input("1.Price Notifier\n2.Stock Notifier: "))
    path = os.getcwd() + '\mixkit-morning-clock-alarm-1003.wav'
    price_og = price(page,soup)
    print(f"Price - {price_og}")
    if inpt == 1:
        price_limit = int(input("Enter the Price Threshold: "))
        while True:
            if price_limit >= price(page,soup):
                webbrowser.open(URL)
                try:
                    playsound(path)
                except PlaysoundException:
                    path = os.getcwd() + '/mixkit-morning-clock-alarm-1003.wav'
                    playsound(path)
                except:
                    pass
            else:
                time.sleep(10)
                print("Running..")
                continue
            break
    elif inpt == 2:
        while True:
            if stock(page,soup) is  None:
                webbrowser.open(URL)
                try:
                    playsound(path)
                except PlaysoundException:
                    path = os.getcwd() + '/mixkit-morning-clock-alarm-1003.wav'
                    playsound(path)
                except:
                    pass
            else:
                time.sleep(10)
                print("Running..")
                continue
            break

if __name__ == "__main__":
    main()