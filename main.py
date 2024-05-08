from oracle_DML import Scraping, OracleProcess
from selenium_p import Selenium_Process
from connect import ConnectDatabase
from datetime import datetime

headers = {
    "User-Agent": "Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F122.0.0.0+Safari%2F537.36"}


time_detail=datetime.strftime(datetime.now(),'%X')
print(time_detail)

url_list=Selenium_Process("https://kontakt.az/notbuk-ve-kompyuterler/komputerler/notbuklar").get_href_list()

connect_oracle = ConnectDatabase()
for url in url_list:
    soup = Scraping(url, headers)
    data = soup.get_tag_value({
        "url": soup.url,
        "h1": {"class": "page-title"},
        "div": {"class": "prodCart__prices product-desktop-block"}
    })
    insert = OracleProcess().insert_product(url=data["url"], title=data["title"], price=data["price"], con_oracle=connect_oracle)
    print(insert)
    del soup.url
    del soup
    #del OracleProcess
connect_oracle.connection.commit()
connect_oracle.connection.close()

time_detail=datetime.strftime(datetime.now(),'%X')
print(time_detail)
