# %%
import sys

print("how many total test scores need to be entered? ")
total_test_scores = int(input())
print("You typed: ", total_test_scores)
thislist = []
for i in range(total_test_scores):
    print("Enter score for student #", i+1)
    scores = int(input())
    thislist.append(scores)
    #thislist = scores
    # for y in range(total_test_scores):
    #     thislist.append(scores)
print(thislist)

print("lista de scores: ", len(thislist))


def revisar():
    for item in thislist:
        if  item > 100:
            print("A score over 100 has been entered")
    return item


def revisarMax():
    print("The highest score is: ", max(thislist))
    return


def revisarMin():
    print("the lowest score is: ", min(thislist))
    return


def promedio():
    promedios = sum(thislist)
    total = promedios / total_test_scores
    print("The average for the class is: ", total)
    return


def secondLargestScore():
    length = len(thislist)
    thislist.sort()
    # print("Largest element is:", thislist[length-1])
    # print("Smallest element is:", thislist[0])
    print("Second Largest score is:", thislist[length-2])
    # print("Second Smallest element is:", thislist[1])

    return


# '''After dropping the two lowest scores, the average is 95.0.'''

print("lista actual",thislist)
def dropTwoLowestScores():
    thislist.sort()
    del thislist[0]
    thislist.remove(min(thislist))
    print(thislist)
    promedios2 = sum(thislist)
    print("suma", promedios2)
    total2 = promedios2 / len(thislist)
    print("The average for the class is: ", total2)

    #print("new list: ", remover)
    return


revisar()
revisarMax()
revisarMin()
promedio()
secondLargestScore()
dropTwoLowestScores()

'''OUTPUT
PS C:\Users\anayeli\Documents\PythonScientificProgramming> python testscores.py
how many total test scores need to be entered?
4
('You typed: ', 4)
('Enter score for student #', 1)
34
('Enter score for student #', 2)
77
('Enter score for student #', 3)
101
('Enter score for student #', 4)
89
[34, 77, 101, 89]
('lista de scores: ', 4)
('lista actual', [34, 77, 101, 89])
A score over 100 has been entered
('The highest score is: ', 101)
('the lowest score is: ', 34)
('The average for the class is: ', 75)
('Second Largest score is:', 89)
[89, 101]
('suma', 190)
('The average for the class is: ', 95)'''

# %%
