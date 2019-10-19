team1 = raw_input("ENTER TEAM 1: ")
team2 = raw_input("ENTER TEAM 2: ")

flag = 0

with open('nfl1978-2013.csv', 'r') as f:
    for line in f:#lee cada linea
        if team1 in line: #me regresara un lista donde esten los falcos en cada juego
            flag = 1
            #print(line)
            
            if team2 in line:# este if tenia que estar indentado dentro del otro por que el otro nos devolvia una lista de solo falcons
                separar_palabras = line.split(",")
                #print(separar_palabras[1:])#que imprima desde aqui no significa que la lista cambio sus index
                
                if separar_palabras[2] == "0" or separar_palabras[4] == "0":
                    print("one of the teams was shut out: ")
                    print(separar_palabras)
                else:
                    flag = 1

if flag:
    print("For the rest of the other games, both teams scored more that 0\n")
'''OUTPUT
ENTER TEAM 1: Baltimore Colts
ENTER TEAM 2: Dallas Cowboys
one of the teams was shut out:
['09/04/1978', 'Baltimore Colts', '0', 'Dallas Cowboys', '38\n']
For the rest of the other games, both teams scored more that 0

ENTER TEAM 1: Atlanta Falcons
ENTER TEAM 2: Denver Broncos
In each game, both teams scored more that 0

ENTER TEAM 1: Baltimore Colts
ENTER TEAM 2: Dallas Cowboys
['Baltimore Colts', '0', 'Dallas Cowboys', '38\n']
['Dallas Cowboys', '37', 'Baltimore Colts', '13\n']
'''