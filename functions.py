from sys import exit
import requests
from bs4 import BeautifulSoup as bs

def Bot_Exit():
    exit()

def GetToken() -> str:
    try:
        with open("token", "r") as f:
            return f.readline().strip()
    except FileNotFoundError:
        print("토큰 파일이 존재하지 않습니다.")
        with open("token", "w") as f:
            pass
        print("토큰을 입력해주십시오.")
        Bot_Exit()
        
def GetVersion() -> str:
    try:
        with open("token", "r") as f:
            return f.readline().strip()
    except FileNotFoundError:
        print("토큰 파일이 존재하지 않습니다.")
        with open("token", "w") as f:
            pass
        print("토큰을 입력해주십시오.")
        Bot_Exit()
        
def FindGameSearch(name: str):
    name.replace(" ", "%20")
    url = f"https://steamdb.info/instantsearch/?query={name}&refinementList%5BappType%5D%5B0%5D=Game"
    response = requests.get(url)
    code = response.status_code
    if response.status_code == 200:
        html = response.text
        soup = bs(html, 'html.parser')
        
        Find_Lists = soup.select('li.ais-Hits-item')

        return Find_Lists
    
        
        