from bs4 import  BeautifulSoup
import requests
from playsound import playsound
import webbrowser

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
        price(page,soup,URL)
def main():
    while True:
        page = requests.get(URL, headers = header)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            title = soup.find("span", class_ = "B_NuCI").get_text().strip()
            break
        except:
            pass
    print(title+"\n")
    price_og = price(page,soup)
    print(f"Price - {price_og}")
    price_limit = int(input("Enter the Price Threshold: "))
    sound = input("Enter path to your music: ")
    while True:
        if(price_limit >= price(page,soup)):
            webbrowser.open(URL)
            playsound(sound)
            break
        else:
            continue
if __name__ == "__main__":
    main()


