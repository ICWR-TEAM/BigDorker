import SearchEngine

s = SearchEngine

class Main:
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
        result = s.bing_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                result = s.bing_search(query, self.page)
                for res in result:
                    print("Title:", res["title"])
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
        result = s.duckduckgo_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                result = s.duckduckgo_search(query, self.page)
                for res in result:
                    print("Title:", res["title"])
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
        result = s.google_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                result = s.google_search(query, self.page)
                for res in result:
                    print("Title:", res["title"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["deskripsi"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")


    def call_yahoo_search(self, query, page):
        result = s.yahoo_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                self.page += 7
                result = s.yahoo_search(query, self.page)
                for res in result:
                    print("Title:", res["title"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["description"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

    def call_yandex_search(self, query, page):
        result = s.yandex_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                self.page += 1
                result = s.yandex_search(query, self.page)
                for res in result:
                    print("Title:", res["title"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["description"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

    def call_ask_search(self, query = "", page = ""):
        result = s.ask_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                self.page += 1
                result = s.ask_search(query, self.page)
                for res in result:
                    print("Title:", res["title"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["description"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

    def call_mojeek_search(self, query = "", page = ""):
        result = s.mojeek_search(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                result = s.mojeek_search(query, self.page)
                for res in result:
                    print("Title:", res["title"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["description"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

    def call_searx_search(self, query = "", page = ""):
        result = s.searx_seach(query, page)
        for res in result:
            print("=========================================")
            print("Title:", res["title"])
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
                result = s.searx_seach(query, self.page)
                for res in result:
                    print("Title:", res["title"])
                    print("Domain:", res["data"]["domain"])
                    print("URL:", res["data"]["url"])
                    print("Description:", res["data"]["description"])
                    print("=========================================")        
            elif inp_next == '2':
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

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

if __name__ == "__main__":
    print(Main().write_figlet())
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
            Main(inp_searchEngine)
    except:
        print("Your choice is wrong!")
