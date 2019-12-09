import requests
from bs4 import BeautifulSoup
import urllib.request

def cooling():
    page = requests.get('http://www.worldclimate.com/cgi-bin/grid.pl?gr=N39W105')
    soup = BeautifulSoup(page.content, 'html.parser')
    AllheatingDays = soup.find_all('a', href=True, text='Cooling Degree Days')
    for link in AllheatingDays:
        linkTag = link.get('href')

        network_cooling = []
        # Podemos manipular linkTag para solo obtener el pedazo de estring que queremos
        #print(linkTag,"PRINTING EACH TAG")
        new_url = 'http://www.worldclimate.com/cgi-bin/' + linkTag
        
        page_2 = requests.get(new_url)
        soup_2 = BeautifulSoup(page_2.content, 'html.parser')

        antero_table = soup_2.find_all('td')[1].get_text()        

        list_of_strings_cooling = antero_table.split()  # split by space
        
        list_of_strings_cooling = list_of_strings_cooling[:13]
        
        #print(list_of_strings_cooling)
        #print(type(list_of_strings_cooling))
        # diccionario = {}
        # diccionario[linkTag[-7:]] = {}
        # diccionario[linkTag[-7:]]['Colling Degree Days'] = list_of_strings_cooling
        # #print(diccionario)

    return list_of_strings_cooling

# return a list outside de fnc
nerwork_cooling = cooling()
print(nerwork_cooling)

diccionario = {}
diccionario['linkTag[-7:]'] = {}
diccionario['linkTag[-7:]']['Colling Degree Days'] = nerwork_cooling
print(diccionario)

