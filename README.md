# Big Dorker
![Screenshot from 2024-02-24 19-46-36](https://github.com/ICWR-TEAM/BigDorker/assets/45759837/ea190d4d-8cc8-4013-bc42-905d029f2a3c)

Big Dorker is a console-based tool used for dorking on multiple popular search engines such as Google, DuckDuckGo, Bing, Yahoo, Yandex, Ask, Mojeek, and Searx. Dorking is a search technique used by security researchers and information security professionals to find sensitive information that is inadvertently exposed in publicly available databases and documents online.

## What new??
- Addition of output file for dorking results.
- addition of automated dorking feature.

## Key Features

- Automatic Dorking: Perform automatic dorking on various search engines using predefined queries and dorks.
- Search Engine Support: Supports multiple popular search engines including Google, DuckDuckGo, Bing, Yahoo, Yandex, Ask, Mojeek, and Searx.
- Result Processing: Process search results and present them in a readable and understandable format.
- Information Security: Useful in penetration testing and security audits, allowing security researchers to find sensitive information that may be exploitable or vulnerable to attacks.
- Risk Analysis: Enables users to conduct risk analysis on the discovered information and identify potential security vulnerabilities or weaknesses in their infrastructure.

## Installation

1. Ensure Python is installed on your system.
2. Download or clone this repository into a local directory.
3. Open a terminal or command prompt and navigate to the directory where you saved the source code.
4. Run `pip install -r requirements.txt` to install the required dependencies.
5. Run Big Dorker by executing the command `python search.py --o 'manual'/'auto'`.

## Usage

```bash
billy@icwr:~/projects$ python3 search.py -h

usage: search.py [-h] -o OPTION

options:
  -h, --help            show this help message and exit
  -o OPTION, --option OPTION
                        Give your choice ('manual' or 'auto')

```


## Suggestion!!!

When performing auto dorking, it's advisable to use a delay of 4 to avoid potential access blocking.

## Another picture
![Screenshot from 2024-02-24 19-41-23](https://github.com/ICWR-TEAM/BigDorker/assets/45759837/78c11fa8-7b12-41bb-90fe-1735eeb38190)
![Screenshot from 2024-02-24 19-41-48](https://github.com/ICWR-TEAM/BigDorker/assets/45759837/d6356b7a-b43e-4bd5-ac82-6c43f3cc0465)

## Miscellaneous

- **Contributions**: Feel free to explore and customize Big Dorker according to your needs and preferences. You can also contribute to this project by submitting bug reports, feature requests, or code enhancements through GitHub.
- **License**: This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

Let me know if you need further adjustments!
