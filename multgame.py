# %%
print("how many total test scores need to be entered? ")
total_test_scores = int(input())
print("You typed: ", total_test_scores)
thislist = []
for i in range(total_test_scores):
    print("Enter score for student #", i)
    scores = int(input())
    thislist.append(scores)
    #thislist = scores
    # for y in range(total_test_scores):
    #     thislist.append(scores)
print(thislist)

# %%
N = 10
listi = []
if (N > 0):
    for i in range(10):
        listi.append(i)
print(listi)

# %%
