#%%
d = {}
print(type(d))
#tuples = ()
with open('stars.dat','r') as f:
    data = f.readlines()#.read reads all the words
    print(data)
    
# Each line as string is split at space character. First component is used as key and second as value
    for line in data:
        print(line)
        (keys, val, val2, val3) = line.split(",")
        d[(keys, val, val2, val3)] = val
    print(type(d))
    print(len(d))
    print(d)
'''output:
{('Alpha Centauri A', '    4.3', '  0.26', '      1.56\n'): '    4.3', ('Alpha Centauri B', '    4.3', '  0.077', '     0.45\n'): '    4.3', ('Alpha Centauri C', '    4.2', '  0.00001', '   0.00006\n'): '    4.2', ("Barnard's Star", '      6.0', '  0.00004', '   0.0005\n'): '      6.0', ('Wolf 359', '            7.7', '  0.000001', '  0.00002\n'): '            7.7', ('BD +36 degrees 2147', ' 8.2', '  0.0003', '    0.006\n'): ' 8.2', ('Luyten 726-8 A', '      8.4', '  0.000003', '  0.00006\n'): '      8.4', ('Luyten 726-8 B', '      8.4', 
'  0.000002', '  0.00004\n'): '      8.4', ('Sirius A', '            8.6', '  1.00', '      23.6\n'): '            8.6', ('Sirius B', ' 
           8.6', '  0.001', '     0.003\n'): '            8.6', ('Ross 154', '            9.4', '  0.00002', '   0.0005\n'): '
  9.4'}
'''
# %%
