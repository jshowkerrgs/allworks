from time import sleep

import requests
from bs4 import BeautifulSoup as bs

data = []

for p in range(0, 1):
    print(p)
    url = f"https://www.nexusmods.com/valheim/mods/?BH={p}"
    r = requests.get('https://www.nexusmods.com/valheim/mods/')
    sleep(2)
    soup = bs(r.content, 'html5lib')

    mods = soup.find_all('li', class_='mod-tile')

    for mod in mods:
        mod_url = mod.find('div', class_='mod-tile-left').find('div',
                                                               class_='tile-desc motm-tile').find(
            'div', class_='tile-content').find('p', class_='tile-name').find('a').get('href')
        mod_name = mod.find('div', class_='mod-tile-left').find('div',
                                                                class_='tile-desc motm-tile').find(
            'div', class_='tile-content').find('p', class_='tile-name').find('a').text
        mod_size = mod.find('div', class_='mod-tile-left').find('div',
                                                                class_='tile-data').find('ul', class_='clearfix').find(
            'li', class_='sizecount inline-flex').find('span').text
        mod_likes = mod.find('div', class_='mod-tile-left').find('div',
                                                                 class_='tile-data').find('ul', class_='clearfix').find(
            'li', class_='endorsecount inline-flex').find('span').text
        mod_downloads = mod.find('div', class_='mod-tile-left').find('div',
                                                                     class_='tile-data').find('ul',
                                                                                              class_='clearfix').find(
            'li', class_='downloadcount inline-flex')  # js ,import selenium
        data.append([mod_url, mod_name, mod_size, mod_likes, mod_downloads])
for mod in data:
    print(f"Mod URL: {mod[0]}")
    print(f"Mod name: {mod[1]}")
    print(f"Mod size: {mod[2][1:]}")
    print(f"Mod likes: {mod[3]}")
    print(f"Mod download count: {mod[4]}")
