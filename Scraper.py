from winotify import Notification, audio
from colorama import Fore
from Modules import RequestAsProxy
import requests
import pyfiglet
import webbrowser
import time
import os

group_API_Format = 'https://groups.roblox.com/v1/groups/'

def getGroupInformationFromID(ID: int): # Getter function for returning group information with the ID given
    GroupInformation = requests.get(group_API_Format + str(ID)).json() # RequestAsProxy.get(group_API_Format + str(ID)).json()
    return GroupInformation

def checkGroup(GroupInformation: dict): #Checks if group meets the requirements
    if GroupInformation['owner'] == None and GroupInformation['publicEntryAllowed']:
        return True

def startScraping(Start, End, Delay):
    ID = Start
    while ID <= End:
        os.system(f'title Group #{ID}')
        try:
            Group = getGroupInformationFromID(ID)
            if checkGroup(Group):
                link = f'https://www.roblox.com/groups/{str(ID)}'
                webbrowser.open(link)
                showToastNotification('GROUP FOUND!', 'A OWNERLESS GROUP HAS BEEN FOUND!')
                print(Fore.GREEN + f'[FOUND] {link}')
            ID += 1
        except Exception:
            print(Fore.RED + 'Failed to check group!')
        time.sleep(Delay)

def showToastNotification(Title: str, Message: str): # A toast notification function for the lazy
    Toast = Notification('Group Scraper', Title, Message)
    Toast.set_audio(audio.Reminder, False)
    Toast.show()

def loadBanner():
    print(Fore.MAGENTA + pyfiglet.figlet_format('Group Scraper', 'slant'))

def start():
    Delay = input('Delay every scrape [INT]> ')
    Start = input('Start scraping at [INT]> ')
    End = input('End scraping at [INT]> ')
    startScraping(int(Start), int(End), float(Delay))

if __name__ == '__main__':
    loadBanner()
    start()