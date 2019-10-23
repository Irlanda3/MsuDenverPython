import sys

# v0 = 3;g = 9.81; t = 0.6 y = v0*t - 0.5*g*t**2 print y
# only v0 and t from comand line
try:
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
    g = 9.81
    y = v0*t - 0.5*g*t**2
    print(y)
except IndexError:
    print("Provide vo and t! ")
    print("enter v0: ")
    v0 = float(raw_input())
    print("enter t: ")
    t = float(raw_input())
    g = 9.81
    y = v0*t - 0.5*g*t**2
    print(y)
    sys.exit(1)  # abort

    '''output:

PS C:\Users\anayeli\Documents\PythonScientificProgramming> python ball_cml_qa.py
Provide vo and t!
enter v0:
3
enter t:
0.6
0.0342'''