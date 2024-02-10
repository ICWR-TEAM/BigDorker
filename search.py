from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from urllib.parse import urlparse, quote_plus, unquote
import re

class Main:
        
    def __init__(self, inp_searchEngine=""):
        # /////inidiedit
        self.inp_searchEngine = inp_searchEngine
        if self.inp_searchEngine == "1":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            self.call_google_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "2":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            self.call_duckduckgo_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "3":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_bing_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "99":
            pass
        else:
            print("Your keywoard is wrong!")

    def call_bing_search(self, query, page):
        result = self.bing_search(query, page)
        # print(result)
        for res in result:
            print("=========================================")
            print("Title:", res["judul"])
            print("Domain:", res["data"]["domain"])
            print("URL:", res["data"]["url"])
            print("Description:", res["data"]["description"])
        print("=========================================")
        while True:
            if not result:
                print("Search not found!")
                break
            print("1. Next")
            print("2. Stop")
            inp_next = input("Next or stop (Enter number): ")
            print("=========================================")
            if inp_next == '1':
                print(self.write_figlet())
                self.page += 10
                result = self.bing_search(query, self.page)
                # print(result)
                for res in result:
                    print("Title:", res["judul"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["description"])
                    print("=========================================")
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

    def call_duckduckgo_search(self, query, page):
        result = self.duckduckgo_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["judul"])
            print("Domain:", res["data"]["domain"])
            print("URL:", res["data"]["url"])
            print("Description:", res["data"]["description"])
        print("=========================================")
        while True:
            if not result:
                print("Search not found!")
                break
            print("1. Next")
            print("2. Stop")
            inp_next = input("Next or stop (Enter number): ")
            print("=========================================")
            if inp_next == '1':
                print(self.write_figlet())
                self.page += 10
                result = self.duckduckgo_search(query, self.page)
                for res in result:
                    print("Title:", res["judul"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["description"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")


    def call_google_search(self, query, page):
        result = self.google_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["judul"])
            print("Domain:", res["data"]["domain"])
            print("URL:", res["data"]["url"])
            print("Description:", res["data"]["deskripsi"])
        print("=========================================")
        while True:
            if not result:
                print("Search not found!")
                break
            print("1. Next")
            print("2. Stop")
            inp_next = input("Next or stop (Enter number): ")
            print("=========================================")
            if inp_next == '1':
                print(self.write_figlet())
                self.page += 10
                result = self.google_search(query, self.page)
                for res in result:
                    print("Title:", res["judul"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["deskripsi"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

    def bing_search(self, query, page_start):
        result_array = []
        req_res = self.req("https://www.bing.com/search?q=" + quote_plus(str(query)) + "&first="+ str(page_start) + "&FORM=PERE", "bing").text
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
                    "description": description_replace_str_web
                }
            }
            if "Related searches" in title_res or "Explore further" in title_res or "Images of" in title_res:
                continue
            result_array.append(join_dict)
        return result_array

    def duckduckgo_search(self, query="", page_start=0):
        result_array = []
        req_res = self.req("https://html.duckduckgo.com/html/?q="+ quote_plus(str(query)) +"&b=" + str(page_start), "duckduckgo").text
        result_bs4 = BeautifulSoup(req_res, "html.parser")
        res_title = result_bs4.find_all("h2", class_="result__title")
        res_url = result_bs4.find_all("a", class_="result__a")
        res_deskripsi = result_bs4.find_all("a", class_="result__snippet")
        for title, url, description in zip(res_title, res_url, res_deskripsi):
            parse_url = urlparse(url["href"].split("uddg=")[1].split("&amp;")[0].split("&rut=")[0]).geturl()
            decode_url = unquote(parse_url)
            join_dict = {
                "judul": title.a.get_text(),
                "data": {
                    "url": decode_url,
                    "domain": urlparse(decode_url).netloc,
                    "description": description.get_text()
                }
            }
            result_array.append(join_dict)
        return result_array
            

    def google_search(self, query="", page_start=0):
        result_array = []
        req_res = self.req("https://www.google.com/search?q=" + quote_plus(str(query)) + "&start=" + str(page_start), "google").text
        result = BeautifulSoup(req_res, "html.parser")
        res_title = result.find_all("h3", class_="LC20lb")
        res_deskripsi = result.find_all("div", class_="VwiC3b")
        span_urls = result.find_all('span', jscontroller="msmzHf")
        for title, description, urls in zip(res_title, res_deskripsi, span_urls):
            join_dict = {
                "judul": title.get_text(),
                "data": {
                    "url": urls.find("a").get("href"),
                    "domain": urlparse(urls.find("a").get("href")).netloc,
                    "deskripsi": description.get_text()
                }
            }
            result_array.append(join_dict)
        return result_array

    def proc(self):
        pass

    def ua(self):
        return UserAgent().chrome

    def req(self, url, req_headers):
        if req_headers == "duckduckgo":
            header = {
            'Authority': 'html.duckduckgo.com',
            'Method': 'GET',
            'Scheme': 'https',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
            'Cache-Control': 'max-age=0',
            'Cookie': 'kl=be-fr',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            }
        elif req_headers == "google":
            header = {"User-Agent": self.ua()}
        elif req_headers == "bing":
            header = {"User-Agent": self.ua()}

        req = requests.get(url, headers = header)
        return req
    
    def write_figlet(self):
        return """
______  _         ______               _                
| ___ \(_)        |  _  \             | |               
| |_/ / _   __ _  | | | |  ___   _ __ | | __  ___  _ __ 
| ___ \| | / _` | | | | | / _ \ | '__|| |/ / / _ \| '__|
| |_/ /| || (_| | | |/ / | (_) || |   |   < |  __/| |   
\____/ |_| \__, | |___/   \___/ |_|   |_|\_\ \___||_|   
            __/ |                                       
           |___/                                                    
        """

# inp_searchEngine = int(input("Seach engine: "))  
# Main(inp_searchEngine)
    

# Main().bing_search()



if __name__ == "__main__":
    print("""
______  _         ______               _                
| ___ \(_)        |  _  \             | |               
| |_/ / _   __ _  | | | |  ___   _ __ | | __  ___  _ __ 
| ___ \| | / _` | | | | | / _ \ | '__|| |/ / / _ \| '__|
| |_/ /| || (_| | | |/ / | (_) || |   |   < |  __/| |   
\____/ |_| \__, | |___/   \___/ |_|   |_|\_\ \___||_|   
            __/ |                                       
           |___/                                                                                                                     
""")
    print("1. Google")
    print("2. DuckDuckGo")
    print("3. Bing")
    print("99. Exit program")
    try:
        inp_searchEngine = input("Search engine: ")
        if inp_searchEngine == "99":
            print("Exiting the program...")
        else:
            Main(inp_searchEngine)
    except:
        print("Your choice is wrong!")















    # if inp_searchEngine == 1:
    #     Main(inp_searchEngine)
    # elif inp_searchEngine == "99":
    #     print("Exiting the program...")
    # else:
    #     print("Invalid input. Please enter either 1 or 99.")