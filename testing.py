from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urlparse, quote_plus, unquote
import re
import requests
import json
def yahoo_search(query = "", page_start = 1):
    result_array = []
    req_res = req(
        "https://yandex.com/search/?text=" + quote_plus(str(query)) + "&p=" + str(page_start),
        "yandex"
    ).text
    result = BeautifulSoup(req_res, "html.parser")
    res_title = result.find_all("h2", class_="OrganicTitle-LinkText Typo Typo_text_l Typo_line_m organic__url-text")
    res_description = result.find_all("div", class_="TextContainer OrganicText organic__text text-container Typo Typo_text_m Typo_line_m")
    res_url = result.find_all("a", class_="OrganicTitle-Link")
    for title, description, url in zip(res_title, res_description, res_url):
        parse_url = urlparse(url.get("href")).netloc
        join_dict = {
            "title": title.get_text(),
            "data": {
                "url": url.get("href"),
                "domain": parse_url,
                "description": description.get_text()
            }
        }
        result_array.append(join_dict)
    return result_array

def ua():
    return UserAgent().chrome


def req(url, req_headers):
    if req_headers == "duckduckgo":
        header = {
            "Authority": "html.duckduckgo.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }
    elif req_headers == "google":
        header = {"User-Agent": ua()}
    elif req_headers == "bing":
        header = {"User-Agent": ua()}
    else:
        header = {"User-Agent": ua()}

    req = requests.get(url, headers=header)
    return req


print(yahoo_search("indo", page_start=1))