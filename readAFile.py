
import sys
# print("Enter a team name: ")
# u = (input())
# #with open("nfl1978-2013.csv","w") as infile:
# with open("airPollutionClass.txt",'w') as outfile:
#     #read una linea nada mas
#     line = outfile.readline()
#     print(line)

# with open('airPollutionClass.txt','r') as f:
#     #f.read will be saved in ram
#      f_contents = f.read()
#      print(f_contents)

# -------------
# with open('airPollutionClass.txt','r') as f:
#     #f.read will NOT be saved in ram
#      f_contents = f.readlines()
#      print(f_contents)

# -----------
user = raw_input("enter animal:")# i am having issues woth oython 2 and 3 it seems like i am running version 2 instead of 3

flag = 0

with open('airPollutionClass.txt', 'r') as f:
    # iterate the file
    for line in f:
        # print(line)sjdc
        # if the user enter a
        #  team then display that info
        if user in line: 
            flag = 1
#            print("lo encntramos")
 #       else:
  #          print("no lo encontramos")
if flag:
    print("found conejo: ", user)
# ------
# skip in chapter 4  
# 4.8
# 4.9
# 4.10
# 4.2
# 4.4.1