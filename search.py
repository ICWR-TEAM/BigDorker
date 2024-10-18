import SearchEngine
import argparse, time
import utils

s = SearchEngine

class System:

    def proc_manual(self, engine, query_search, pages, value, name_file, file, proxies):
        many_search = 0
        page = pages
        for res in value:
            requests_value = {
                "title": res["title"],
                "domain": res['data']['domain'],
                "url": res['data']['url'],
                "description": res['data']['description']
            }
            utils.write_file(file, query_search, requests_value)
            utils.print_value(query_search, requests_value)
        while True:
            print("1. Next")
            print("2. Stop")
            inp_next = input("Next or stop (Enter number): ")
            print("=========================================")
            if inp_next == '1':
                print(utils.write_figlet())

                # callback function
                if engine == "bing":
                    result = s.bing_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 10
                elif engine == "google":
                    result = s.google_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 10
                elif engine == "duckduckgo":
                    result = s.duckduckgo_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 10
                elif engine == "yahoo":
                    result = s.yahoo_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 7
                elif engine == "yandex":
                    result = s.yandex_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 1
                elif engine == "ask":
                    result = s.ask_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 1
                elif engine == "mojeek":
                    result = s.mojeek_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 10
                elif engine == "searx":
                    result = s.searx_search(query_search, page, proxies)
                    if not result:
                        many_search += 1
                    page += 10

                if many_search > 2 and not result:
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
                    utils.write_file(file, query_search, requests_value)
                    utils.print_value(query_search, requests_value)
            elif inp_next == '2':
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

    def proc_auto(self, engine, query_search, pages, delay, name_file, file, proxies = False):
        for list_query in utils.list_querys():
            query = query_search + " " + list_query
            if engine == "google":
                result = s.google_search(query, pages, proxies)
            elif engine == "duckduckgo":
                result = s.duckduckgo_search(query, pages, proxies)
            elif engine == "bing":
                result = s.bing_search(query, pages, proxies)
            elif engine == "yahoo":
                result = s.yahoo_search(query, pages, proxies)
            elif engine == "yandex":
                result = s.yandex_search(query, pages, proxies)
            elif engine == "ask":
                result = s.ask_search(query, pages, proxies)
            elif engine == "mojeek":
                result = s.mojeek_search(query, pages, proxies)
            elif engine == "searx":
                result = s.searx_search(query, pages, proxies)
                
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
                    utils.write_file(file, query, requests_value)
                    utils.print_value(query, requests_value)

                utils.next_loading()
                if not result:
                    utils.not_result(query)
                print("=========================================\n")
                time.sleep(int(delay))
            except KeyboardInterrupt:
                print("\n[*]Stopped: File is in output/" + name_file + ".txt")
                break


class Main_manual(System):
    global s
    def __init__(self, inp_searchEngine="", proxies = False):
        self.inp_searchEngine = inp_searchEngine
        if self.inp_searchEngine == "1":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "google"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "2":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "duckduckgo"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "3":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "bing"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "4":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "yahoo"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "5":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "yandex"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "6":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "ask"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "7":
            self.page = 11
            self.inp_query = input("Enter dorking: ")
            engine = "mojeek"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "8":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "searx"
            self.call_search(engine, self.inp_query, self.page, proxies)
        elif self.inp_searchEngine == "99":
            pass
        elif self.inp_searchEngine == "":
            pass
        else:
            print("Your keywoard is wrong!")

    def call_search(self, engine, query, page, proxies = False):
        name_file = engine + "_" + utils.date_file()
        file = open("output/" + name_file + ".txt", "w")
        if engine == "google":
            result = s.google_search(query, page, proxies)
        elif engine == "duckduckgo":
            result = s.duckduckgo_search(query, page, proxies)
        elif engine == "bing":
            result = s.bing_search(query, page, proxies)
        elif engine == "yahoo":
            result = s.yahoo_search(query, page, proxies)
        elif engine == "yandex":
            result = s.yandex_search(query, page, proxies)
        elif engine == "ask":
            result = s.ask_search(query, page, proxies)
        elif engine == "mojeek":
            result = s.mojeek_search(query, page, proxies)
        elif engine == "searx":
            result = s.searx_search(query, page, proxies)
        self.proc_manual(engine, query, page, result, name_file, file, proxies) #process
        file.close()



class Main_auto(System):
    global s
    def __init__(self, inp_searchEngine = "", inp_time = "", proxies = False):
        self.inp_searchEngine = inp_searchEngine
        delay = inp_time if inp_time else 4
        if self.inp_searchEngine == "1":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "google"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "2":
            self.page = 10
            self.inp_query = input("Enter dorking: ")
            engine = "duckduckgo"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "3":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "bing"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "4":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "yahoo"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "5":
            self.page = 0
            self.inp_query = input("Enter dorking: ")
            engine = "yandex"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "6":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "ask"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "7":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "mojeek"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "8":
            self.page = 1
            self.inp_query = input("Enter dorking: ")
            engine = "searx"
            self.call_search(engine, self.inp_query, self.page, delay, proxies)
        elif self.inp_searchEngine == "99":
            pass
        elif self.inp_searchEngine == "":
            pass
        else:
            print("Your keywoard is wrong!")

    def call_search(self, engine, query, page, delay, proxies = False):
        name_file = engine + "_" + utils.date_file()
        file = open("output/" + name_file + ".txt", "w")
        self.proc_auto(engine, query, page, delay, name_file, file, proxies)
        file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--option", help="Give your choice ('manual' or 'auto')", type=str, required=True)
    parser.add_argument("-x","--proxy", help="Give your proxy (use http/https)", type=str, required=False)
    args = parser.parse_args()
    if args.option == "manual":
        utils.print_choice()
        
        try:
            inp_searchEngine = input("Search engine: ")
            if inp_searchEngine == "99":
                print("Exiting the program...")
            else:
                Main_manual(inp_searchEngine)
        except:
            print("Your choice is wrong!")
            
    elif args.option == "auto":
        utils.print_choice()
        
        try:
            inp_searchEngine = input("Search engine: ")
            if inp_searchEngine == "99":
                print("Exiting the program...")
            else:
                inp_time =  input("Delay/second(default 4/s): ")
                Main_auto(inp_searchEngine, inp_time)
        except:
            print("Your input is wrong(please check documentation)!")