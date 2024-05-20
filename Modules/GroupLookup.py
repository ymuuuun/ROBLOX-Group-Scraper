from Modules import Proxilama
import requests

# The module that looks for ownerless groups

def lookupGroup(groupID: str, useProxy=False) -> bool:
    urlformat = f'https://groups.roblox.com/v1/groups/{groupID}'
    json: dict

    if useProxy:
        json = Proxilama.get(urlformat).json()
    else:
        json = requests.get(urlformat).json()

    if json['owner'] == None and json['publicEntryAllowed'] and not json['isLocked']:
        return True
    else:
        return False
