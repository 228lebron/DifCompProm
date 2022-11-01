import requests
from requests import Response
import pandas as pd
from bs4 import BeautifulSoup as BS
from scraper.constants import REQUEST_HEADER, REQUEST_COOKIES

def request_url(url: str) -> Response:
    try:
        response = requests.get(url, headers=REQUEST_HEADER, cookies=REQUEST_COOKIES, timeout=10)
        return response
    except requests.exceptions.RequestException as e:
        print(e)




class CompelScraper():
    def __init__(self, part_number: str) -> None:
        # super().__init__()
        self.part_number = part_number
        self.url = f"https://www.electronshik.ru/search?query={self.part_number}&in_stock=1&view=table"

    def get_data(self) -> pd.DataFrame:
        response = request_url(self.url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return pd.DataFrame()
        df = pd.read_html(response.text)[0]
        return df







