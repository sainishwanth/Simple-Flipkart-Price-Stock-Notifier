from bs4 import  BeautifulSoup
import requests
from playsound import playsound
import webbrowser
import time

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
        stock(page,soup)

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
    price_og = price(page,soup)
    print(f"Price - {price_og}")
    sound = input("Enter path to your music: ")
    if inpt == 1:
        price_limit = int(input("Enter the Price Threshold: "))
        while True:
            if(price_limit >= price(page,soup)):
                webbrowser.open(URL)
                playsound(sound)
                break
            else:
                time.sleep(10)
                print("Running..")
                continue
    elif inpt == 2:
        while True:
            if not stock(page,soup):
                webbrowser.open(URL)
                playsound(sound)
                break
            else:
                time.sleep(10)
                print("Running..")
                continue

if __name__ == "__main__":
    main()


