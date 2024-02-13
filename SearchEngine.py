from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urlparse, quote_plus, unquote
import re
import requests


def proc():
    pass


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

def bing_search(query, page_start):
    result_array = []
    req_res = req(
        "https://www.bing.com/search?q="
        + quote_plus(str(query))
        + "&first="
        + str(page_start)
        + "&FORM=PERE",
        "bing",
    ).text
    result_bs4 = BeautifulSoup(req_res, "html.parser")
    res_title = result_bs4.find_all("h2", style_="")
    res_decription = result_bs4.find_all("p")
    for title, description in zip(res_title, res_decription):
        description_replace_str_web = description.get_text().replace("Web", "")
        title_res = title.get_text()
        url_res = ""
        for a in title.find_all("a"):
            url_res += a.get("href")
        domain_res = urlparse(url_res).netloc
        join_dict = {
            "judul": title_res,
            "data": {
                "url": url_res,
                "domain": domain_res,
                "description": description_replace_str_web,
            },
        }
        if (
            "Related searches" in title_res
            or "Explore further" in title_res
            or "Images of" in title_res
        ):
            continue
        result_array.append(join_dict)
    return result_array


def duckduckgo_search(query="", page_start=0):
    result_array = []
    req_res = req(
        "https://html.duckduckgo.com/html/?q="
        + quote_plus(str(query))
        + "&b="
        + str(page_start),
        "duckduckgo",
    ).text
    result_bs4 = BeautifulSoup(req_res, "html.parser")
    res_title = result_bs4.find_all("h2", class_="result__title")
    res_url = result_bs4.find_all("a", class_="result__a")
    res_deskripsi = result_bs4.find_all("a", class_="result__snippet")
    for title, url, description in zip(res_title, res_url, res_deskripsi):
        parse_url = urlparse(
            url["href"].split("uddg=")[1].split("&amp;")[0].split("&rut=")[0]
        ).geturl()
        decode_url = unquote(parse_url)
        join_dict = {
            "judul": title.a.get_text(),
            "data": {
                "url": decode_url,
                "domain": urlparse(decode_url).netloc,
                "description": description.get_text(),
            },
        }
        result_array.append(join_dict)
    return result_array


def google_search(query="", page_start=0):
    result_array = []
    req_res = req(
        "https://www.google.com/search?q="
        + quote_plus(str(query))
        + "&start="
        + str(page_start),
        "google",
    ).text
    result = BeautifulSoup(req_res, "html.parser")
    res_title = result.find_all("h3", class_="LC20lb")
    res_deskripsi = result.find_all("div", class_="VwiC3b")
    span_urls = result.find_all("span", jscontroller="msmzHf")
    for title, description, urls in zip(res_title, res_deskripsi, span_urls):
        join_dict = {
            "judul": title.get_text(),
            "data": {
                "url": urls.find("a").get("href"),
                "domain": urlparse(urls.find("a").get("href")).netloc,
                "deskripsi": description.get_text(),
            },
        }
        result_array.append(join_dict)
    return result_array

def yahoo_search(query = "", page_start = 1):
    result_array = []
    req_res = req(
        "https://search.yahoo.com/search?p=" + quote_plus(str(query)) + "&b=" + str(page_start),
        "yahoo"
    ).text
    result = BeautifulSoup(req_res, "html.parser")
    res_title = result.find_all("a", class_="d-ib fz-20 lh-26 td-hu tc va-bot mxw-100p")
    res_description = result.find_all("p", class_="fz-14 lh-22 mah-44 ov-h d-box fbox-ov fbox-lc2")
    res_url = res_title
    for title, url, description in zip(res_title, res_url, res_description):
        title_parse = title.get_text().split(" › ")[-1]
        url_parse = unquote(urlparse(url.get("href").split("RU=")[1].split("/RK=")[0]).geturl())
        join_dict = {
            "judul": title_parse,
            "data": {
                "url": url_parse,
                "domain": urlparse(url_parse).netloc,
                "description": description.get_text()
            }
        }
        result_array.append(join_dict)
    return result_array

def yandex_search(query = "", page_start = 0):
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
            "judul": title.get_text(),
            "data": {
                "url": url.get("href"),
                "domain": parse_url,
                "description": description.get_text()
            }
        }
        result_array.append(join_dict)
    return result_array
    