import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
from random import choice
from bs4 import BeautifulSoup
import requests


os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO")
os.system('cls' if os.name == 'nt' else 'clear')

print('      _______ _      __________________       _______ _______ _______ _______\n'
      '     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )\n'
      '     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |\n'
      '     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |\n'
      '     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |\n'
      '     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |\n'
      '     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |\n'
      '     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)\n')
print("[+] ABOUT SCRIPT:")
print("[-] With this script, you can getting unlimited GB on Warp+.")
print("[-] Version: 4.0.0")
print("--------")
print("[+] THIS SCRIPT CODDED BY ALIILAPRO")
print("[-] SITE: aliilapro.github.io")
print("[-] TELEGRAM: aliilapro")
print("--------")

referrer = input("[#] Enter the WARP+ ID:")


def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def get_proxy():
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='proxylisttable').find_all('tr')[
          1:11]

    proxies = []

    for tr in trs:
        tds = tr.find_all('td')
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        schema = 'https' if 'yes' in tds[6].text.strip() else 'http'
        proxy = {'schema': schema, 'address': ip + ':' + port}
        proxies.append(proxy)
    return choice(proxies)


def run():

    p_g = get_proxy()
    proxy = {p_g['address']}

    try:
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'
                   }
        req = urllib.request.Request(url, data, headers)
        p = urllib.request.ProxyHandler({'http': f'{proxy}'})
        opener = urllib.request.build_opener(p)
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print(error)


g = 0
b = 0

while True:

    result = run()

    if result == 200:

        g = g + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
        print("")
        animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%",
                     "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%",
                     "[■■■■■■■■■■] 100%"]
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
            sys.stdout.flush()
        print(f"\n[-] WORK ON ID: {referrer}")
        print(f"[:)] {g} GB has been successfully added to your account.")
        print(f"[#] Total: {g} Good {b} Bad")
        print("[*] After 18 seconds, a new request will be sent.")
        time.sleep(18)
    else:

        b = b + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
        print("")
        print("[:(] Error when connecting to server.")
        print(f"[#] Total: {g} Good {b} Bad")
