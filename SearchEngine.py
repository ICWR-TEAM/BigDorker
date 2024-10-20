from bs4 import BeautifulSoup
from urllib.parse import urlparse, quote_plus, unquote
import json
import utils


#####################################
#            Bing Search            #
#####################################
def bing_search(query, page_start, proxies = False):
    result_array = []
    req_res = utils.req(
        "https://www.bing.com/search?q="
        + quote_plus(str(query))
        + "&first="
        + str(page_start)
        + "&FORM=PERE",
        "bing",
        proxies
    )
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
            "title": title_res,
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


#####################################
#        DuckDuckGo Search          #
#####################################
def duckduckgo_search(query="", page_start=0, proxies = False):
    result_array = []
    req_res = utils.req(
        "https://html.duckduckgo.com/html/?q="
        + quote_plus(str(query))
        + "&b="
        + str(page_start),
        "duckduckgo",
        proxies
    )
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
            "title": title.a.get_text(),
            "data": {
                "url": decode_url,
                "domain": urlparse(decode_url).netloc,
                "description": description.get_text(),
            },
        }
        result_array.append(join_dict)
    return result_array


#####################################
#            Google Search          #
#####################################
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
    result = BeautifulSoup(req_res, "html.parser")
    res_title = result.find_all("h3", class_="LC20lb")
    res_deskripsi = result.find_all("div", class_="VwiC3b")
    span_urls = result.find_all("span", jscontroller="msmzHf")
    for title, description, urls in zip(res_title, res_deskripsi, span_urls):
        join_dict = {
            "title": title.get_text(),
            "data": {
                "url": urls.find("a").get("href"),
                "domain": urlparse(urls.find("a").get("href")).netloc,
                "description": description.get_text(),
            },
        }
        result_array.append(join_dict)
    return result_array


#####################################
#            Yahoo Search           #
#####################################
def yahoo_search(query = "", page_start = 1, proxies = False):
    result_array = []
    req_res = utils.req(
        "https://search.yahoo.com/search?p=" + quote_plus(str(query)) + "&b=" + str(page_start),
        "yahoo",
        proxies
    )
    result = BeautifulSoup(req_res, "html.parser")
    res_title = result.find_all("a", class_="d-ib fz-20 ls-024 lh-19 td-hu tc va-bot mxw-100p mt-8")
    res_description = result.find_all("p", class_="fc-dustygray fz-14 lh-22 ls-02 mah-44 ov-h d-box fbox-ov fbox-lc2")
    res_url = res_title
    for title, url, description in zip(res_title, res_url, res_description):
        title_parse = title.get_text().split(" › ")[-1]
        url_parse = unquote(urlparse(url.get("href").split("RU=")[1].split("/RK=")[0]).geturl())
        join_dict = {
            "title": title_parse,
            "data": {
                "url": url_parse,
                "domain": urlparse(url_parse).netloc,
                "description": description.get_text()
            }
        }
        result_array.append(join_dict)
    return result_array


#####################################
#           Yandex Search           #
#####################################
def yandex_search(query = "", page_start = 0, proxies = False):
    result_array = []
    req_res = utils.req(
        "https://yandex.com/search/?text=" + quote_plus(str(query)) + "&p=" + str(page_start),
        "yandex",
        proxies
    )
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
    
    
#####################################
#             ASK Search            #
#####################################
def ask_search(query = "", page_start = 0, proxies = False):
    result_array = []
    req_res = utils.req(
        "https://www.ask.com/web?q=" + quote_plus(str(query)) + "&page=" + str(page_start),
        "ask",
        proxies
    )
    result = BeautifulSoup(req_res, "html.parser")
    result_json_ask = []

    # crawling json data ask search
    for script_tag in result.find_all("script"):
        # Mengekstrak teks dari tag <script>
        script_text = script_tag.string
        if script_text:
            # Mencari data JSON dalam teks tag <script>
            if 'window.MESON.initialState' in script_text:
                # Membagi teks berdasarkan tanda sama dengan (=) dan mengambil bagian kedua
                json_data = script_text.split('window.MESON.initialState = ')[1].strip()
                # Menghapus karakter non-JSON pada awal dan akhir string
                json_data = json_data.split('window.MESON.loadedLang = "en";')[0].strip()
                json_data = json_data.rstrip(";").strip()
                # Menampilkan data JSON
                # res_title += json.loads(json_data)
                parsed_json = json.loads(json_data)
                result_json_ask.append(parsed_json)
                # res_title += json.loads(json_data)

    for i in result_json_ask:
        for asd in i["search"]["webResults"]["results"]:
            url = asd["url"]
            title = asd["title"]
            description = asd["abstract"]
            join_dict = {
                "title": url,
                "data": {
                    "url": url,
                    "domain": urlparse(url).netloc,
                    "description": description
                }
            }
            result_array.append(join_dict)
    return result_array


#####################################
#           Mojeek Search           #
#####################################
def mojeek_search(query = "", page_start = 0, proxies = False):
    result_array = []
    req_res = utils.req(
        "https://www.mojeek.com/search?q=" + quote_plus(str(query)) + "&s=" + str(page_start),
        "mojeek",
        proxies        
    )
    result = BeautifulSoup(req_res, "html.parser")
    res_title = result.find_all("a", class_="title")
    res_url = res_title
    res_description = result.find_all("p", class_="s")
    for title, url, description in zip(res_title, res_url, res_description):
        join_dict = {
            "title": title.get_text(),
            "data": {
                "url": url.get("href"),
                "domain": urlparse(url.get("href")).netloc,
                "description": description.get_text()
            }
        }
        result_array.append(join_dict)
    return result_array

#####################################
#            Searx Search           #
#####################################
def searx_search(query = "", page_start = "", proxies = False):
    result_array = []
    req_res = utils.req(
        "https://searx.thegpm.org/?q=" + quote_plus(str(query)),
        "searx",
        proxies
    )
    result = BeautifulSoup(req_res, "html.parser")
    res_title = result.find_all("h4", class_="result_header")
    res_description = result.find_all("p", class_="result-content")

    for title, description in zip(res_title, res_description):
        res_url = title.a.get('href')
        domain = urlparse(res_url).netloc
        join_dict = {
            "title": title.get_text(),
            "data": {
                "url": res_url,
                "domain": domain,
                "description": description.get_text()
            }
        }
        result_array.append(join_dict)
    return result_array
