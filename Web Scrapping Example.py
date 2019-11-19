#import urllib
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm") as url:
    web_page = url.read()
        #specify the url
        #web_page = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    page = urllib.request.urlopen(web_page)

    soup = BeautifulSoup(page, 'html.parser')

    print(soup)

    artist_name_list =soup.find(class_='BodyTest')
    print(artist_name_list)

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')

    artist_name_list_items = artist_name_list.find_all('a')
    print(artist_name_list_items)

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        print(names)
        links = 'https://web.archive.org' + artist_name.get('href')
        print(links)



