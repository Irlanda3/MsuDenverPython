import requests
from bs4 import BeautifulSoup
import urllib.request

def heating(data):
    page = requests.get('http://www.worldclimate.com/cgi-bin/grid.pl?gr=N39W105')
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup)# prints all html used in the page
    AllheatingDays = soup.find_all('a', href=True, text='Heating Degree Days')
    for link in AllheatingDays:
        linkTag = link.get('href')

        # Podemos manipular linkTag para solo obtener el pedazo de estring que queremos
        print(linkTag,"PRINTING EACH TAG")
        print(type(linkTag))

        #linkTag[-7:]

        new_url = 'http://www.worldclimate.com/cgi-bin/' + linkTag
        # print(new_url)

        page_2 = requests.get(new_url)
        soup_2 = BeautifulSoup(page_2.content, 'html.parser')

        # we ignore the C at index 0
        antero_table = soup_2.find_all('td')[1].get_text()
        #print(antero_table)  # imprime los numeros con el C y F

        list_of_strgs = antero_table.split()  # split by space
        #nota: esta separados pero cada numero cuenta como un digit aqun que esten juntos
        # print(list_of_strgs)
        # print(type(antero_table))
        # print(len(antero_table))

        list_of_strgs = list_of_strgs[:13]
        print(list_of_strgs)

        diccionario = {}
        diccionario[linkTag[-7:]] = {}
        diccionario[linkTag[-7:]]['Heating Degree Days'] = list_of_strgs
        print(diccionario)

   
    return

    
nom = heating('data.pl?ref=N39W105+1306+050263C')

def cooling():
    page = requests.get('http://www.worldclimate.com/cgi-bin/grid.pl?gr=N39W105')
    soup = BeautifulSoup(page.content, 'html.parser')
    AllheatingDays = soup.find_all('a', href=True, text='Cooling Degree Days')
    for link in AllheatingDays:
        linkTag = link.get('href')

        # Podemos manipular linkTag para solo obtener el pedazo de estring que queremos
        print(linkTag,"PRINTING EACH TAG")
        print(type(linkTag))

        #linkTag[-7:]

        new_url = 'http://www.worldclimate.com/cgi-bin/' + linkTag
        # print(new_url)

        page_2 = requests.get(new_url)
        soup_2 = BeautifulSoup(page_2.content, 'html.parser')

        antero_table = soup_2.find_all('td')[1].get_text()        

        list_of_strgs = antero_table.split()  # split by space
        
        list_of_strgs = list_of_strgs[:13]
        print(list_of_strgs)

        diccionario = {}
        diccionario[linkTag[-7:]] = {}
        diccionario[linkTag[-7:]]['Colling Degree Days'] = list_of_strgs
        print(diccionario)

    return