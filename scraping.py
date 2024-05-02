from bs4 import BeautifulSoup
from datetime import time
import requests


class Scraping:
    soup_data = None

    def __init__(self, url, head):
        self.url = url
        self.head = head
        r_data = requests.get(self.url, self.head)
        print("Take data...")
        self.soup_data = BeautifulSoup(r_data.text, "html.parser")

    def get_value(self):
        return self.soup_data

    def clear_value(self=None, tg=None, value=None):
        if str(tg) == "h1":
            return value.text.strip()
        else:
            price_value = value.text.split("₼")[0].strip().replace(",", ".")
            return price_value.replace(".", "", 1)

    def get_tag_value(self, dict_values):
        dict_values_new = {}
        dict_values_new["url"] = self.url
        for tag, attr in dict_values.items():
            if str(tag) == "h1":
                dict_values_new["title"] = self.clear_value(tg=tag, value=self.soup_data.find(tag, attrs=attr))
            else:
                dict_values_new["price"] = self.clear_value(value=self.soup_data.findAll("strong")[2])
        return dict_values_new
