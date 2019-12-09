import requests
from bs4 import BeautifulSoup
import urllib.request

page = requests.get('http://www.worldclimate.com/cgi-bin/grid.pl?gr=N39W105')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)# prints all html used in the page
AllheatingDays = soup.find_all('a', href=True, text='Heating Degree Days')

# Note that find_all returns a list, so we’ll have to loop through, or use list indexing, it to extract text:
heatingDaysAntero = soup.find_all('a', href='data.pl?ref=N39W105+1306+050263C')
for tag in heatingDaysAntero:
    linkTag = tag.get('href')

    new_url = 'http://www.worldclimate.com/cgi-bin/' + linkTag
    # print(new_url)

    page_2 = requests.get(new_url)
    soup_2 = BeautifulSoup(page_2.content, 'html.parser')

    antero_table = soup_2.find_all('td')[1].get_text()# we ignore the C at index 0
    print(antero_table)#imprime los numeros con el C y F
    
    list_of_strgs = antero_table.split()#split by space
    #nota: esta separados pero cada numero cuenta como un digit aqun que esten juntos
    print(list_of_strgs)
    print(type(antero_table))
    print(len(antero_table))

    list_of_strgs = list_of_strgs[:13]
    print(list_of_strgs)

    diccionario = {}
    #float_list_days = list(map(int, list_of_strgs))
    
#nota: podeoms separalo por slice y luego lo convertimos a float. 
# diccionario['Heating Degree Days'] = {}
# diccionario['Heating Degree Days'] = list_of_strgs
# print(diccionario)
diccionario['050263C'] = {}
diccionario['050263C']['Heating Degree Days'] = list_of_strgs
print(diccionario)

#diccionario['']

    
        
