from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urlparse, quote_plus, unquote
import re
import requests
import json
import utils


def google_search(query="", page_start=0, proxies = False):
    result_array = []
    req_res = utils.req(
        "https://www.google.com/search?q="
        + quote_plus(str(query))
        + "&start="
        + str(page_start),
        "google",
        proxies
    )
    # result = BeautifulSoup(req_res, "html.parser")
    # res_title = result.find_all("h3", class_="LC20lb")
    # res_deskripsi = result.find_all("div", class_="VwiC3b")
    # span_urls = result.find_all("span", jscontroller="msmzHf")
    # for title, description, urls in zip(res_title, res_deskripsi, span_urls):
    #     join_dict = {
    #         "title": title.get_text(),
    #         "data": {
    #             "url": urls.find("a").get("href"),
    #             "domain": urlparse(urls.find("a").get("href")).netloc,
    #             "description": description.get_text(),
    #         },
    #     }
    #     result_array.append(join_dict)
    return req_res

def ua():
    return UserAgent().chrome


# def req(url, req_headers):
#     if req_headers == "duckduckgo":
#         header = {
#             "Authority": "html.duckduckgo.com",
#             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
#         }
#     elif req_headers == "google":
#         header = {"User-Agent": ua()}
#     elif req_headers == "bing":
#         header = {"User-Agent": ua()}
#     else:
#         header = {"User-Agent": ua()}

#     req = requests.get(url, headers=header)
#     return req


print(google_search("a", "", "http://google.com"))