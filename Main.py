from Modules import GroupLookup
import webbrowser
from winotify import Notification, audio
import time
import os
import pathlib
from colorama import Fore

RootFolder = pathlib.Path(__file__).parent
Banner = '''                                                                                                                          
   __ _ _ __ ___  _   _ _ __    ___  ___ _ __ __ _ _ __   ___ _ __ 
  / _` | '__/ _ \| | | | '_ \  / __|/ __| '__/ _` | '_ \ / _ \ '__|
 | (_| | | | (_) | |_| | |_) | \__ \ (__| | | (_| | |_) |  __/ |   
  \__, |_|  \___/ \__,_| .__/  |___/\___|_|  \__,_| .__/ \___|_|   
   __/ |               | |                        | |              
  |___/                |_|                        |_|              
'''

def openNotification(title: str, msg: str):
    toast = Notification(app_id='Group Scraper', title=title, msg=msg)
    toast.set_audio(audio.Reminder, False)
    toast.show()

def startScraping(delay, start, end, useProxies): 
    currentid = start
    while currentid <= end:
        os.system(f'Title Progress : {currentid}/{end}')
        try:
            validGroup = GroupLookup.lookupGroup(currentid, useProxies)
            if validGroup:
                link = f'https://www.roblox.com/groups/{currentid}'
                print(Fore.GREEN + f'[FOUND] {link}')
                openNotification('A GROUP HAS BEEN FOUND!', f'AFTER {currentid} IDs')
                webbrowser.open(link)
                with open(f'{RootFolder}\Groups.txt', 'a') as file:
                    file.write(f'\n{link}')
            currentid += 1
        except Exception as error:
            print(Fore.RED + f'Could not find group! : {type(error)} {error}')
        time.sleep(delay)

def start():
    print(Fore.MAGENTA + Banner)

    delay = input('Delay [float]> ')
    useProxies = input('Use proxies [y/n]> ')
    start = input('Start at [int]> ')
    end = input('End at [int]> ')

    if useProxies == 'y':
        useProxies = True
    else:
        useProxies = False

    os.system('cls')
    startScraping(float(delay), int(start), int(end), useProxies)

if __name__ == '__main__':
    start()