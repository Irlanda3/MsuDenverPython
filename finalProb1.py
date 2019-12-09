'''{’050263C’: {’Heating Degree Days’: [900.0, 757.0, 718.0, 536.0, 387.0, 223.0, 127.0,163.0, 283.0, 473.0,
                                     685.0, 871.0, 6129.0], 
                                     ’Cooling Degree Days’: [0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}}'''
import requests
from bs4 import BeautifulSoup

page =  requests.get('http://www.worldclimate.com/cgi-bin/grid.pl?gr=N39W105')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
week = soup.find( href='data.pl?ref=N39W105+1306+050263C')
#week = soup.find( 'a href = data.pl?ref=N39W105+1306+050263C')
# print(type(week))
# print(week)

# antero = soup.find( href= 'data.pl?ref=N39W105+1308+050263C')
# print(antero)

diccionario_1 = {}
diccionario_2 = {}

# Collect degrees into a list
degree_list = []

items_tabla = week.find_all('table')

for heating_days in items_tabla:
    # lista = degree_list.append(heating_days)
    degree_list.extend(heating_days.find_all('900'))
print(degree_list)
