#%%
'''

OUTPUT:



---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
 in 
     13     return
     14 
---> 15 test_double((2,1,1),(0.1), lst, (1,2),(3+4j), "hello")

 in test_double(a, b, lst, c, d, e)
      5 lst = [10, 11, 12, 13, 14, 15]
      6 def test_double(a,b,lst,c,d,e):#no necesito argumentos
----> 7     assert (a) == 4, "should be another answer"
      8     assert abs((b) - 0.2) < 1E-15
      9     assert ([lst]) == [1, 2, 1, 2]

AssertionError: should be another answer'''

lst = [10, 11, 12, 13, 14, 15]
def test_double(a,b,lst,c,d,e):
    assert (a) == 4, "should be another answer"
    assert abs((b) - 0.2) < 1E-15
    assert ([lst]) == [1, 2, 1, 2]
    assert (c) == (1, 2, 1, 2)
    assert (d) == 6+8j
    assert (e) == "hellohello"
    return

test_double((2,1,1),(0.1), lst, (1,2),(3+4j), "hello")



#%%
