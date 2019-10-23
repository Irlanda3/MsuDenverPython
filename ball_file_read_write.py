
def leerFile():
    with open('ball.dat', 'r') as ballData:
        v0 = ballData.readline()
        print(v0)
        lines = []
        for line in ballData:
            lines.append(line)
        print(lines)
    return v0, lines

leerFile()

#Make a test function that generates an input ﬁle, calls 
# the function in a) for reading the ﬁle,
# and checks that the returned data objects are correct.
def testFnc():
    with open('ballTest.dat', 'w') as ballTest:# va a gener uno para ver si esta bn el primero
        leerFile()
        #checar q los objectos son correectos
        assert v0 == 3.00 and assert lines == lines
        if not:
            raise AssertionError()
    return

'''Writeafunctionthatcreates a ﬁle with two nicely formatted columns containing the t values to the left 
and the corresponding y values to the right. Let the t values appear in increasing order 
(note that the input ﬁle does not necessarily have the t values sorted)
y.t/D v0t 0:5gt'''

def dosCol():
    with open('ball.dat', 'r') as ballData:
        v0 = ballData.readline()
        # #print(v0)
        lines = []      
        
        lines = ballData.readlines()                  
            
        print(lines,"\n")      
           
        with open('ball_order.dat', 'w') as ball_order:
            for i in lines:
                
                print >> ball_order, i    
    return
dosCol()

'''OUTPUT
PART A
[Running] python -u "c:\Users\anayeli\Documents\PythonScientificProgramming\ball_file_read_write.py"
v0: 3.00

['t:\n', '0.15592  0.28075   0.36807889 0.35 0.57681501876\n', '0.21342619  0.0519085  0.042  0.27  0.50620017 0.528\n', '0.2094294  0.1117  0.53012  0.3729850  0.39325246\n', '0.21385894  0.3464815 0.57982969 0.10262264\n', '0.29584013  0.17383923\n']
PART B
[Running] python -u "c:\Users\anayeli\Documents\PythonScientificProgramming\ball_file_read_write.py"
  File "c:\Users\anayeli\Documents\PythonScientificProgramming\ball_file_read_write.py", line 14
SyntaxError: Non-ASCII character '\xef' in file c:\Users\anayeli\Documents\PythonScientificProgramming\ball_file_read_write.py on line 14, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

[Done] exited with code=1 in 1.211 seconds
PART c
[Running] python -u "c:\Users\anayeli\Documents\PythonScientificProgramming\tempCodeRunnerFile.py"
(['t:\n', '0.15592  0.28075   0.36807889 0.35 0.57681501876\n', '0.21342619  0.0519085  0.042  0.27  0.50620017 0.528\n', '0.2094294  0.1117  0.53012  0.3729850  0.39325246\n', '0.21385894  0.3464815 0.57982969 0.10262264\n', '0.29584013  0.17383923\n'], '\n')
'''