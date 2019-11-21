with open('stars.dat','r') as f:
   lines = f.readlines()

output = {}#dictionary

for s in lines: 
    split_line = s.split(",")
    first = split_line[0].strip()
    output[first] = {}
    output[first][first] = split_line[1].strip()
    pairs = []
    for i in range(0, len(split_line[2:]), 2):
        pairs.append(split_line[2:][i:i+2])

    for pair in pairs:
        day = pair[0].strip()
        output[first].setdefault(day, []).append(pair[1].strip())

print(output)

'''OUTPUT:
{'Alpha Centauri A': {'Alpha Centauri A': '4.3', '0.26': ['1.56']}, 'Alpha Centauri B': {'Alpha Centauri B': '4.3', '0.077': ['0.45']}, 
'Alpha Centauri C': {'Alpha Centauri C': '4.2', '0.00001': ['0.00006']}, "Barnard's Star": {"Barnard's Star": '6.0', '0.00004': ['0.0005']}, 'Wolf 359': {'Wolf 359': '7.7', '0.000001': ['0.00002']}, 'BD +36 degrees 2147': {'BD +36 degrees 2147': '8.2', '0.0003': ['0.006']}, 'Luyten 726-8 A': {'Luyten 726-8 A': '8.4', '0.000003': ['0.00006']}, 'Luyten 726-8 B': {'Luyten 726-8 B': '8.4', '0.000002': ['0.00004']}, 'Sirius A': {'Sirius A': '8.6', '1.00': ['23.6']}, 'Sirius B': {'Sirius B': '8.6', '0.001': ['0.003']}, 'Ross 154': {'Ross 154': 
'9.4', '0.00002': ['0.0005']}}
'''