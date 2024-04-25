import fake_headers
import bs4
import requests


class Parser:
    @staticmethod
    def get_names(gender: str) -> list:
        url = f"https://kakzovut.ru/{gender}.html"
        headers_gen = fake_headers.Headers(browser="firefox", os="win")
        response = requests.get(url=url, headers=headers_gen.generate())
        html_data = response.text
        soup = bs4.BeautifulSoup(html_data, "lxml")
        data = soup.find_all(class_="nameslist")
        names = [item.text for item in data]

        return names
