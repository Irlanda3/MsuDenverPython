'''The Magic Eval Function:The eval functions takes a string as argument and evaluates this string as a Python
expression. The result of an expression is an object. Consider'''

r = eval("1+2")
r
print(type(r))
print(r)



'''error handling'''
# import sys
# try:
#     C = float(sys.argv[1])
# except:
#     print ("esta mal")
#     sys.exit(1) # abort
# F = 9.0*C/5 + 32
# print (F )# el formato del libro a mi no me funcuina en mi codigo me causa un error