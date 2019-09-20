#%%
#Anayeli Ochoa | Homework # 1
'''Chapter 1 Exercises:  1.3, 1.4, 1.6, 1.9, 1.10, 1.12, 1.15, 1.16, 1.17, 1.18
Exercise 1.3: Derive and compute a formula
Can a newborn baby in Norway expect to live for one billion (10^9) seconds? Write
a Python program for doing arithmetics to answer the question.
Filename: seconds2years.
This homework is due on Thursday, September 5, 2019 at the beginning of class.
'''
#Ex 1.3

billion_sec = 10**9
print(billion_sec) # 1,000,000,000

#how many hours is that. sec to hrs
sec_to_min = billion_sec / 60
print(sec_to_min)

min_to_hrs = sec_to_min / 60
print(min_to_hrs, "Hours")

hrs_to_days = min_to_hrs / 24
print(hrs_to_days," Days can a baby live")

days_to_years = hrs_to_days / 365
print("total years", days_to_years)

if days_to_years > 1:
    print("THIS IS NOT CONSIDER A NEW BORN! IT is an adult of", days_to_years," Years!")





'''RESULTS:
1000000000
16666666.666666666
277777.77777777775 Hours
11574.074074074073  Days can a baby live
total years 31.709791983764582
THIS IS NOT CONSIDER A NEW BORN! IT is an adult of 31.709791983764582  Years!

'''