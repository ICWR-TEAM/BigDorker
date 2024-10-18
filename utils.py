from datetime import datetime
import argparse, time, sys
from curl_cffi import requests


def ua():
    return UserAgent().chrome

def req(url, req_headers):
    get_data = requests.get(url, impersonate="chrome")
    response = get_data.text
    return response

#####################################################
#                 System at search.py               #
#####################################################

def list_querys(key = ""):
    list = open("listdork.txt", "r").read()
    split_list = list.split("\n")
    if key == "":
        return split_list
    else:
        return split_list[int(key)]
    
def print_choice():
    print(write_figlet())
    print("1. Google")
    print("2. DuckDuckGo")
    print("3. Bing")
    print("4. Yahoo!")
    print("5. Yandex")
    print("6. Ask")
    print("7. Mojeek")
    print("8. Searx")
    print("99. Exit program")
    
def write_figlet():
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
    
def date_file():
    now = datetime.now()
    formatted_time = now.strftime("%d_%m_%Y-%H_%M_%S")
    return formatted_time

def write_file(file, query_search, value):
    file.write("=========================================\n")
    file.write(f"Query search: {query_search}\n")
    file.write(f"Title: {value['title']}\n")
    file.write(f"Domain: {value['domain']}\n")
    file.write(f"URL: {value['url']}\n")
    file.write(f"Description: {value['description']}\n")

def print_value(query_search, value):
    print("=========================================")
    print(f"Query search: {query_search}")
    print(f"Title: {value['title']}")
    print(f"Domain: {value['domain']}")
    print(f"URL: {value['url']}")
    print(f"Description: {value['description']}")
    print("=========================================")
    
def loading_animation(frames=20, chars=r"/—\|", delay=0.1):
    for i in range(frames):
        sys.stdout.write(chars[i % len(chars)])
        sys.stdout.flush()
        time.sleep(delay)  
        sys.stdout.write("\b") 
        
def next_loading():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("=========================================\n")
    sys.stdout.write("Next search ")
    loading_animation()
    sys.stdout.write("\n")
    sys.stdout.flush()
    
def not_result(query):
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write(f"Query search: {query}")
    sys.stdout.write("\nSearch not found...\n")
    sys.stdout.flush()