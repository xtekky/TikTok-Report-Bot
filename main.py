#-------------------------------------------------------------------------------------------------
# X-Reporter by Tekky
# Copyright (c) 2022 Tekky. All rights reserved.
# I am not responsible for any damage caused by your use of this software.
#-------------------------------------------------------------------------------------------------

from __future__ import division
import requests, os, threading, time, random
from pystyle import *
from fake_useragent import UserAgent as ua



def main(userid):
    global headers, x, z, prox

    headers = {
        "headers": ua().random
    }

    try:
        if requests.get(f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&object_id={userid}&reason=317&report_type=user').json()['status_code'] == 0:
            x += 1
            print(Colorate.Horizontal(Colors.green_to_white, f'       [*] Succesfully reported {x} times [id={userid}]', 1))
        else:
            z = z + 1
            #print(Colorate.Horizontal(Colors.red_to_yellow, f'       [*] Failed to report {z} times [id={userid}]', 1))
    except:
        z = z + 1
        #print(Colorate.Horizontal(Colors.red_to_yellow, f'       [*] Failed to report {z} times [id={userid}]', 1))


def title():
    global x, z
    while True:
        total = x+z
        try:
            os.system(f'title Tekky (c) 2022 - X-Reporter ^| Target: {user} ^| Reports: {x} ^| Failed: {z} ^| Total requests: {total} ^| Speed: {round(total/(time.time() - start_time), 2)}/s' if os.name == 'nt' else '')
        except:
            os.system(f'title Tekky (c) 2022 - X-Reporter ^| Target: {user} ^| Reports: {x} ^| Failed: {z} ^| Total requests: {total}' if os.name == 'nt' else '')
        time.sleep(0.7)

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title Tekky (c) 2022 - X-Reporter' if os.name == 'nt' else '')
    x = 0
    z = 0
    prox = set()
    txt = '''
        _     _       ______ _______  _____   _____   ______ _______ _______  ______
         \___/       |_____/ |______ |_____] |     | |_____/    |    |______ |_____/
        _/   \_      |    \_ |______ |       |_____| |    \_    |    |______ |    \_
                                                               Made with <3 by Tekky'''

    print(Colorate.Horizontal(Colors.blue_to_purple, txt, 1))

    with open("proxies.txt", "r") as f: 
        for line1 in f.readlines():
            prox.add(line1.strip())
        
    user = Write.Input("       [?] Username > ", Colors.blue_to_purple, interval=0.001)
    print("")
    
    userid = requests.get(f'https://www.tiktok.com/node/share/user/@{user}', headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}).json()["userInfo"]['user']['id']
    
    
    start_time = time.time()
    
    
    threading.Thread(target=title).start()
    
    while True:
        if threading.active_count() < 10:
            threading.Thread(target=main, args=(userid,)).start()
