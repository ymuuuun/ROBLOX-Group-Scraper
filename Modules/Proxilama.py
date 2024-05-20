import requests
import pathlib
import random

# A module specifically made for the groupscraper
# Use this module if you wish to prevent the ROBLOX API from blocking requests from your IP

# Free proxies are not a good option since most use HTTP (An unsafe version of HTTPS) which can have you vulnerable to MITM attacks, 
# most of the free proxies are transparent, which means the proxy owners can see your IP information, we dont want that, do we?
# I recommend using paid proxies, residential and datacenter proxies.
# But if you wish to use free proxies, use them at your own risk.

RootFolder = pathlib.Path(__file__).parent.parent

def getRandomProxy() -> dict:
    with open(f'{RootFolder}\Proxies.txt', 'r') as file:
        Proxies = file.readlines()
        RandomProxy = f'http://{random.choice(Proxies)}'
        return {'http': RandomProxy, 'https': RandomProxy}

def get(url: str) -> requests.Response:
    Proxy = getRandomProxy()
    Response = requests.get(url, proxies=Proxy)
    return Response