from typing import List
import requests
from bs4 import BeautifulSoup

def get_links(url: str) -> List:
    try:
        response = requests.get(url)
    except:
        return []

    if response.status_code != 200:
        return []

    html_text = response.text

    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", "collectionItemDetails")
    links = []

    for div in divs:
        links.append(div.find("a").get("href"))

    return links