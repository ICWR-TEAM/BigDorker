import SearchEngine
import argparse, time, sys
from datetime import datetime

s = SearchEngine

class System:
    global s

    def date_file(self):
        now = datetime.now()
        formatted_time = now.strftime("%d_%m_%Y-%H_%M_%S")
        return formatted_time

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
    
    def write_file(self, file, query_search, value):
        file.write("=========================================\n")
        file.write(f"Query search: {query_search}\n")
        file.write(f"Title: {value['title']}\n")
        file.write(f"Domain: {value['domain']}\n")
        file.write(f"URL: {value['url']}\n")
        file.write(f"Description: {value['description']}\n")

    def print_value(self, query_search, value):
        print("=========================================")
        print(f"Query search: {query_search}")
        print(f"Title: {value['title']}")
        print(f"Domain: {value['domain']}")
        print(f"URL: {value['url']}")
        print(f"Description: {value['description']}")
        print("=========================================")

    def proc_manual(self, engine, query_search, pages, value, name_file, file):
        page = pages
        for res in value:
            requests_value = {
                "title": res["title"],
                "domain": res['data']['domain'],
                "url": res['data']['url'],
                "description": res['data']['description']
            }
            self.write_file(file, query_search, requests_value)
            self.print_value(query_search, requests_value)
        while True:
            print("1. Next")
            print("2. Stop")
            inp_next = input("Next or stop (Enter number): ")
            print("=========================================")
            if inp_next == '1':
                print(self.write_figlet())

                # callback function
                if engine == "bing":
                    result = s.bing_search(query_search, page)
                    page += 10
                elif engine == "google":
                    result = s.google_search(query_search, page)
                    page += 10
                elif engine == "duckduckgo":
                    result = s.duckduckgo_search(query_search, page)
                    page += 10
                elif engine == "yahoo":
                    result = s.yahoo_search(query_search, page)
                    page += 7
                elif engine == "yandex":
                    result = s.yandex_search(query_search, page)
                    page += 1
                elif engine == "ask":
                    result = s.ask_search(query_search, page)
                    page += 1
                elif engine == "mojeek":
                    result = s.mojeek_search(query_search, page)
                    page += 10
                elif engine == "searx":
                    result = s.searx_search(query_search, page)
                    page += 10

                if not result:
                    print("Search not found!")
                    print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                    break
                for res in result:
                    requests_value = {
                        "title": res["title"],
                        "domain": res['data']['domain'],
                        "url": res['data']['url'],
                        "description": res['data']['description']
                    }
                    self.write_file(file, query_search, requests_value)
                    self.print_value(query_search, requests_value)
            elif inp_next == '2':
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")


class Main_manual(System):
    global s
    def __init__(self, inp_searchEngine=""):
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
        elif self.inp_searchEngine == "4":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_yahoo_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "5":
            self.page = 0
            self.inp_query = input("Enter dorking: ")
            self.call_yandex_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "6":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_ask_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "7":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_mojeek_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "8":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_searx_search(self.inp_query, self.page)
        elif self.inp_searchEngine == "99":
            pass
        elif self.inp_searchEngine == "":
            pass
        else:
            print("Your keywoard is wrong!")

    def call_bing_search(self, query, page):
        engine = "bing"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.bing_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()

    def call_duckduckgo_search(self, query, page):
        engine = "duckduckgo"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.duckduckgo_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()

    def call_google_search(self, query, page):
        engine = "google"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.google_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()

    def call_yahoo_search(self, query, page):
        engine = "yahoo"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.yahoo_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()

    def call_yandex_search(self, query, page):
        engine = "yandex"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.yandex_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()

    def call_ask_search(self, query = "", page = ""):
        engine = "ask"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.ask_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()

    def call_mojeek_search(self, query = "", page = ""):
        engine = "mojeek"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.mojeek_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()

    def call_searx_search(self, query = "", page = ""):
        engine = "searx"
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        result = s.searx_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()



class Main_auto:
    global s
    def __init__(self, inp_searchEngine = "", inp_time = ""):
        self.inp_searchEngine = inp_searchEngine
        delay = inp_time if inp_time else 4
        if self.inp_searchEngine == "1":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            self.call_google_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "2":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            self.call_duckduckgo_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "3":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_bing_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "4":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_yahoo_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "5":
            self.page = 0
            self.inp_query = input("Enter dorking: ")
            self.call_yandex_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "6":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_ask_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "7":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_mojeek_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "8":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            self.call_searx_search(self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "99":
            pass
        elif self.inp_searchEngine == "":
            pass
        else:
            print("Your keywoard is wrong!")


    def call_google_search(self, query, page, delay):
        name_file = "google_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.google_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()


    def call_bing_search(self, query, page, delay):
        name_file = "bing_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.bing_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()

    def call_duckduckgo_search(self, query, page, delay):
        name_file = "duckduckgo_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.duckduckgo_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()


    def call_yahoo_search(self, query, page, delay):
        name_file = "yahoo_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.yahoo_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()

    def call_yandex_search(self, query, page, delay):
        name_file = "yandex_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.yandex_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()

    def call_ask_search(self, query = "", page = "", delay = ""):
        name_file = "ask_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.ask_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()

    def call_mojeek_search(self, query = "", page = "", delay = ""):
        name_file = "mojeek_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.mojeek_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()

    def call_searx_search(self, query = "", page = "", delay = ""):
        name_file = "searx" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        for list_query in self.list_querys():
            query_search = query + " " + list_query
            result = s.searx_search(query_search, page)
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break

                    # print terminal
                    print("=========================================")
                    print(f"Query search: {query_search}")
                    print(f"Title: {res['title']}")
                    print(f"Domain: {res['data']['domain']}")
                    print(f"URL: {res['data']['url']}")
                    print(f"Description: {res['data']['description']}")

                    # write file
                    file.write(f"=========================================\n")
                    file.write(f"Query search: {query_search}\n")
                    file.write(f"Title: {res['title']}\n")
                    file.write(f"Domain: {res['data']['domain']}\n")
                    file.write(f"URL: {res['data']['url']}\n")
                    file.write(f"Description: {res['data']['description']}\n")

                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("=========================================\n")
                sys.stdout.write("Next search ")
                self.loading_animation()
                sys.stdout.write("\n")
                sys.stdout.flush()
                if not result:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Query search: {query_search}")
                    sys.stdout.write("\nSearch not found...\n")
                    sys.stdout.flush()
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
        file.close()

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

    def list_querys(self, key = ""):
        dict = [
            'filetype:env | filetype:ini | filetype:config | filetype:env | filetype:passwd | filetype:htpasswd',
            'intitle:"index of" intext:".env"',
            'intitle:"index of" intext:"docker-compose.yml"',
            'intext:APP_ENV',
            'intext:DB_PASSWORD',
            'intext:aws_access_key_id',
            'intext:aws_secret_access_key',
            'intext:GITHUB_TOKEN',
            'intext:AWS_ACCESS_KEY_ID',
            'intext:AWS_SECRET_ACCESS_KEY',
            'intext:GITHUB_TOKEN',
            'intext:db_password',
            'intext:mysql_password',
            'intext:api_key',
            'intext:api_token',
            'intext:access_token',
            'intext:authorization_token',
            'intext:jwt',
            'intext:jwt_token',
            'intext:password'
            'intitle:index.of',
            'ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini',
            'ext:sql | ext:dbf | ext:mdb',
            'ext:log',
            'ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup',
            'inurl:login',
            'intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"',
            'ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv',
            'ext:php intitle:phpinfo "published by the PHP Group"',
            'inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download',
            'inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor',
            'inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config',
            'inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http',
            'ext:action | ext:struts | ext:do',
            'site:pastebin.com ',
            'site:linkedin.com employees ',
            'inurl:"/phpinfo.php" | inurl:".htaccess" | inurl:"/.git" ' + ' -github',
            'site:*.',
            'site:*.*.',
            'inurl:wp-content | inurl:wp-includes',
            '"index of /" + password.txt', 
            'intitle:"Index Of" inurl:admin', 
            'intitle:"Index of" .git/config', 
            'intitle:"Index of" .env', 
            'ext:log inurl:login password',
            'site:facebook.com inurl:about.php intext:"phone"', 
            'site:linkedin.com intitle:"resume" OR intitle:"cv"', 
            'site:twitter.com intitle:"bio" AND "location"',
            'ext:sql intext:"phpMyAdmin" intitle:"dump" filetype:sql',
            'intitle:"Index of" /admin', 
            'intitle:"Index of" /config', 
            'intitle:"Index of" /database',
            'filetype:sql password', 
            'filetype:log username password',
            'ext:ini password', 
            'ext:sh key', 
            'ext:conf aws_access_key_id'
            ]
        if key == "":
            return dict
        else:
            return dict[int(key)]
    
    def loading_animation(self, frames=20, chars="/—\|", delay=0.1):
        for i in range(frames):
            sys.stdout.write(chars[i % len(chars)])
            sys.stdout.flush()
            time.sleep(delay)  
            sys.stdout.write("\b")  

    def date_file(self):
        now = datetime.now()
        formatted_time = now.strftime("%d_%m_%Y-%H_%M_%S")
        return formatted_time



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--option", help="Give your choice ('manual' or 'auto')", type=str, required=True)
    args = parser.parse_args()
    if args.option == "manual":
        print(System().write_figlet())
        print("1. Google")
        print("2. DuckDuckGo")
        print("3. Bing")
        print("4. Yahoo!")
        print("5. Yandex")
        print("6. Ask")
        print("7. Mojeek")
        print("8. Searx")
        print("99. Exit program")
        try:
            inp_searchEngine = input("Search engine: ")
            if inp_searchEngine == "99":
                print("Exiting the program...")
            else:
                Main_manual(inp_searchEngine)
        except:
            print("Your choice is wrong!")
            
    elif args.option == "auto":
        print(Main_auto().write_figlet())
        print("1. Google")
        print("2. DuckDuckGo")
        print("3. Bing")
        print("4. Yahoo!")
        print("5. Yandex")
        print("6. Ask")
        print("7. Mojeek")
        print("8. Searx")
        print("99. Exit program")
        try:
            inp_searchEngine = input("Search engine: ")
            inp_time =  input("Delay/second(default 4/s): ")
            if inp_searchEngine == "99":
                print("Exiting the program...")
            else:
                Main_auto(inp_searchEngine, inp_time)
        except:
            print("Your input is wrong(please check documentation)!")