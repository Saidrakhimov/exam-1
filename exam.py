# 1-topshiriq
"""
list oz ichiga hamma data type larni oladi va [] qovusw bilanj yoziladi.
list ichidagi hamma narsa no ozini indexi boladi va u lar 0 dan bowlanada
float: sonlar 3.4: 6.7: ga ohshash
string: "" la bn ishilidi
dict:{} qovusla bn yozilib key value boladi:  {"key":"value"}
tuples: obektlarni tartiblangan ozgarmas ketmaketligi  (2345, "salom", 234.4)
set: faqat unique object lani oladi {"a","b"}
boolean: true bn false
"""
# 2-topshiriq
"""
and 2 ta ishni bajaradi: print(2+2 and 4+7) 
not bu: print(not 4==4) shu xolatda false qaytaradi 
or: 2 ta xolatdan 1 taso true qaytarsa true qaytaradi print(not 1 == 1) -> False
"""
# 3-topshiriq
"""
git push: upload qiladi
git init: git ni ishiga tushuradi
git clone [link]: kompga copy qladi
git add [file]: commit qilish ga tayyor qladi
git commit -m "[message]": commit qlgandan keyn nma qganizi yozb qoyas qoganla bilishi uchun 
"""
# 4-topshiriq
"""
__init__()har safar yangi ob'ekt yaratish uchun sinfdan foydalanilganda avtomatik ravishda chaqiriladi.
__init__: bu konstruktor shokolad fabrikadigi qolip: oziz shunaqa orgatgansiz )
"""


# 6- topshiriq
def check_even():
    num = int(input("num: "))
    if num % 2 == 0:
        print(f"{num}even")
    else:
        print(f"{num}odd")


# 8-topshiriq

"""
scraping.py
"""
# qganim shula boldi imthondan otmasam bomidi

"""10- topshiriq:
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

"""

# done 1, 2, 3, 4, 6, 9, 10
# not done 7


# 5-topshiriq
"""
Meros bizga boshqa sinfdan barcha usullar va xususiyatlarni meros qilib oladigan sinfni aniqlash imkonini beradi.

ota sinf - bu meros qilib olingan sinf, uni asosiy sinf deb ham ataladi.

bola sinf - bu boshqa sinfdan meros bo'lib qolgan sinf, hosila sinf deb ham ataladi."""
