
'''
How to append to a list in Python?
append() and extend() in Python
If you append another list onto a list, the first list will be a single object at the end of the list.
extend(): Iterates over its argument and adding each element to the list and extending the list.
The length of the list increases by number of elements in it's argument'''


def evaluarMes(str1):
    with open('high_temps.txt', 'r') as hTemps:
        list1 = []  # tengo que declarlo aqui otherwise cada vez que vaya al for lopp creara uno nuevo y borrara lo anterior guardado
        count = 0
        for line in hTemps:
            if line.startswith(str1):  # index from 0 and so on
                count += 1
                # now we have strings sepaparados por espacio y en index 1
                splitBy = line.split(" ")[1:]
                # print(splitBy)
                for grades in splitBy:

                    list1.append(grades)

        # maxTemp = max(list1)  # imprime el numero mas grande de la lista en total
        # minTemp = min(list1)
        test_list = list(map(float, list1))
        # print test_list
        average = sum(test_list) / count

        print("Average temp: ", average)  # prints the total list
        # print(type(list1))

        listResult = []
        # append results to a list
        for results in list1:

            li = list(map(float, list1))

        listResult.insert(0, max(li))
        listResult.insert(1, min(li))
        listResult.insert(2, average)
        print("kistresults:", listResult)

    return listResult


# ahora write un archivo y esta informacion por cada mes
with open('high_temps_mnth.txt', 'w') as crearFile:
    

                # crea el siguiente mes pero en la sig linea cuando sea llamado este def

        print >>crearFile, evaluarMes("1/")
        print >>crearFile, evaluarMes("2/")
        print >>crearFile, evaluarMes("3/")
        print >>crearFile, evaluarMes("4/")
        print >>crearFile, evaluarMes("5/")
        print >>crearFile, evaluarMes("6/")
        print >>crearFile, evaluarMes("7/")
        print >>crearFile, evaluarMes("8/")
        print >>crearFile, evaluarMes("9/")
        print >>crearFile, evaluarMes("10/")
        print >>crearFile, evaluarMes("11/")
        print >>crearFile, evaluarMes("12/")

'''output:
[Running] python -u "c:\Users\anayeli\Documents\PythonScientificProgramming\monthlytemps.py"
('Average temp: ', 36.483870967741936)
('kistresults:', [37.0, 36.0, 36.483870967741936])
('Average temp: ', 40.714285714285715)
('kistresults:', [45.0, 38.0, 40.714285714285715])
('Average temp: ', 50.806451612903224)
('kistresults:', [57.0, 45.0, 50.806451612903224])
('Average temp: ', 62.4)
('kistresults:', [68.0, 57.0, 62.4])
('Average temp: ', 72.90322580645162)
('kistresults:', [77.0, 68.0, 72.90322580645162])
('Average temp: ', 81.1)
('kistresults:', [84.0, 78.0, 81.1])
('Average temp: ', 85.70967741935483)
('kistresults:', [86.0, 84.0, 85.70967741935483])
('Average temp: ', 84.0)
('kistresults:', [86.0, 81.0, 84.0])
('Average temp: ', 76.3)
('kistresults:', [81.0, 71.0, 76.3])
('Average temp: ', 65.19354838709677)
('kistresults:', [71.0, 59.0, 65.19354838709677])
('Average temp: ', 52.2)
('kistresults:', [58.0, 46.0, 52.2])
('Average temp: ', 41.096774193548384)
('kistresults:', [46.0, 37.0, 41.096774193548384])'''

