
import sys


# with open('airPollutionClass.txt', 'r') as f:
#     with open('air_copy.txt', 'w') as escribir:
#     # iterate the file
#         for line in f:
#             print("Enter a city name: ")
#             user = input()

#             # if the user enter a city then display that info
#             if user == line:
#                 escribir.write(user)
#             else:
#                 print("not found")
# ------
# user = raw_input("Type Number : ")
# search = open("airPollutionClass.txt","w")
# for line in search.readlines():
#     for team in user:
#         # Check if any of the digits provided by the user are in the line.
#         if digit in line:
#             print("was found")
#         else:
#             print("not found")

# with open("airPollutionClass.txt", "r") as infile:
#     with open("air_copy.txt","w") as outfile
#             line = infile.readline()#lee solo la 1 linea y si lee esta ahora empezara en la segunda con el loop
#             while True:#will always go
#                 line = infile.readline()
#                 if line:
#                     outfile.#si hya algo lo imprimira
#                 #otherwise
#                 else:
#                     break

# i am having issues woth oython 2 and 3 it seems like i am running version 2 instead of 3
user = raw_input("enter team name: ")

flag = 0
# este archivo empeiza en cero como las listas
with open('nfl1978-2013.csv', 'r') as f:
    # iterate the file

    for line in f:
        #line.split(",")
        if user in line:
            flag = 1
            print(line[11:])
            # if line.find("0"):
            line.split(",")
    print(line)
                #     print("se encontro falcons 0")

if flag:
    print("found the teams: ", user)


# ahora solo imprime los eqipos llamados y con escore de 0 en uno de los dos

    '''encontrar los equipos en fle file es como un chivas america
    y si uno de los dos tiene score de 0 entonces emprimimos ese partido
    print out all the games involving the 2 teams donde uno
    de los equicos tuvo cero escore
'''
