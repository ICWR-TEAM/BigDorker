import SearchEngine
import argparse, time, sys
from datetime import datetime

s = SearchEngine

class System:
    global s

    def list_querys(self, key = ""):
        list = open("listdork.txt", "r").read()
        split_list = list.split("\n")
        if key == "":
            return split_list
        else:
            return split_list[int(key)]

    def print_choice(self):
        print(self.write_figlet())
        print("1. Google")
        print("2. DuckDuckGo")
        print("3. Bing")
        print("4. Yahoo!")
        print("5. Yandex")
        print("6. Ask")
        print("7. Mojeek")
        print("8. Searx")
        print("99. Exit program")

    def date_file(self):
        now = datetime.now()
        formatted_time = now.strftime("%d_%m_%Y-%H_%M_%S")
        return formatted_time

    def write_figlet(self):
        return r"""
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

    def loading_animation(self, frames=20, chars=r"/—\|", delay=0.1):
        for i in range(frames):
            sys.stdout.write(chars[i % len(chars)])
            sys.stdout.flush()
            time.sleep(delay)  
            sys.stdout.write("\b")  

    def date_file(self):
        now = datetime.now()
        formatted_time = now.strftime("%d_%m_%Y-%H_%M_%S")
        return formatted_time

    def next_loading(self):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.write("=========================================\n")
        sys.stdout.write("Next search ")
        self.loading_animation()
        sys.stdout.write("\n")
        sys.stdout.flush()

    def not_result(self, query):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.write(f"Query search: {query}")
        sys.stdout.write("\nSearch not found...\n")
        sys.stdout.flush()

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

    def proc_auto(self, engine, query_search, pages, delay, name_file, file):
        for list_query in self.list_querys():
            query = query_search + " " + list_query
            if engine == "google":
                result = s.google_search(query, pages)
            elif engine == "duckduckgo":
                result = s.duckduckgo_search(query, pages)
            elif engine == "bing":
                result = s.bing_search(query, pages)
            elif engine == "yahoo":
                result = s.yahoo_search(query, pages)
            elif engine == "yandex":
                result = s.yandex_search(query, pages)
            elif engine == "ask":
                result = s.ask_search(query, pages)
            elif engine == "mojeek":
                result = s.mojeek_search(query, pages)
            elif engine == "searx":
                result = s.searx_search(query, pages)
                
            try:
                for res in result:
                    if not res:
                        print("Search not found!")
                        break
                    requests_value = {
                        "title": res["title"],
                        "domain": res['data']['domain'],
                        "url": res['data']['url'],
                        "description": res['data']['description']
                    }
                    self.write_file(file, query, requests_value)
                    self.print_value(query, requests_value)

                self.next_loading()
                if not result:
                    self.not_result(query)
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break


class Main_manual(System):
    global s
    def __init__(self, inp_searchEngine=""):
        self.inp_searchEngine = inp_searchEngine
        if self.inp_searchEngine == "1":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "google"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "2":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "duckduckgo"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "3":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "bing"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "4":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "yahoo"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "5":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "yandex"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "6":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "ask"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "7":
            self.page = 11
            self.inp_query = input("Enter dorking: ")
            engine = "mojeek"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "8":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "searx"
            self.call_search(engine, self.inp_query, self.page)
        elif self.inp_searchEngine == "99":
            pass
        elif self.inp_searchEngine == "":
            pass
        else:
            print("Your keywoard is wrong!")

    def call_search(self, engine, query, page):
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        if engine == "google":
            result = s.google_search(query, page)
        elif engine == "duckduckgo":
            result = s.duckduckgo_search(query, page)
        elif engine == "bing":
            result = s.bing_search(query, page)
        elif engine == "yahoo":
            result = s.yahoo_search(query, page)
        elif engine == "yandex":
            result = s.yandex_search(query, page)
        elif engine == "ask":
            result = s.ask_search(query, page)
        elif engine == "mojeek":
            result = s.mojeek_search(query, page)
        elif engine == "searx":
            result = s.searx_search(query, page)
        self.proc_manual(engine, query, page, result, name_file, file) #process
        file.close()



class Main_auto(System):
    global s
    def __init__(self, inp_searchEngine = "", inp_time = ""):
        self.inp_searchEngine = inp_searchEngine
        delay = inp_time if inp_time else 4
        if self.inp_searchEngine == "1":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "google"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "2":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "duckduckgo"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "3":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "bing"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "4":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "yahoo"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "5":
            self.page = 0
            self.inp_query = input("Enter dorking: ")
            engine = "yandex"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "6":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "ask"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "7":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "mojeek"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "8":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "searx"
            self.call_search(engine, self.inp_query, self.page, delay)
        elif self.inp_searchEngine == "99":
            pass
        elif self.inp_searchEngine == "":
            pass
        else:
            print("Your keywoard is wrong!")

    def call_search(self, engine, query, page, delay):
        name_file = engine + "_" + self.date_file()
        file = open("output/" + name_file + ".txt", "w")
        self.proc_auto(engine, query, page, delay, name_file, file)
        file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--option", help="Give your choice ('manual' or 'auto')", type=str, required=True)
    args = parser.parse_args()
    if args.option == "manual":
        System().print_choice()
        try:
            inp_searchEngine = input("Search engine: ")
            if inp_searchEngine == "99":
                print("Exiting the program...")
            else:
                Main_manual(inp_searchEngine)
        except:
            print("Your choice is wrong!")
            
    elif args.option == "auto":
        System().print_choice()
        try:
            inp_searchEngine = input("Search engine: ")
            if inp_searchEngine == "99":
                print("Exiting the program...")
            else:
                inp_time =  input("Delay/second(default 4/s): ")
                Main_auto(inp_searchEngine, inp_time)
        except:
            print("Your input is wrong(please check documentation)!")