import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            news_daily = soup.find_all(class_="ddd")

            for news in news_daily:
                print(news.get_text())
        else:
            print("Xato site yozldi", response.status_code)
    except Exception as xato:
        print("fatality ERROR  ozini os ", xato)


url = "https://tribuna.uz/"

scrape_news(url)
