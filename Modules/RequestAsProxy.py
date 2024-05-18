import requests
import pathlib
import random

# WARNING : USING FREE PROXIES IS ABSOLUTELY UNSAFE, SINCE MOST USE HTTP, AND MAKES YOU VULNERABLE TO MITM ATTACKS, OR YOUR INFORMATION BEING LEAKED.
# IT IS RECOMMENDED TO USE A RESIDENTIAL OR DATACENTER PROXY.

RootFolder = pathlib.Path(__file__).parent.parent

def getRandomProxy():
    with open(f'{RootFolder}\ProxiesList.txt', 'r') as file:
        Proxies = file.readlines()
        RandomProxy = f'http://{random.choice(Proxies)}'
        print(RandomProxy)
        return {'http': RandomProxy, 'https': RandomProxy}

def get(URL: str) -> requests.Response: # Requests.get() but if ur a psychopath
    Proxy = getRandomProxy()
    Response = requests.get(URL, proxies=Proxy)
    return Response