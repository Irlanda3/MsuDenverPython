'''For each month, compute the maximum, minimum, and average high temperatures.
 Write the output to a ﬁle named high_temps_mnth.txt. Your output should contain 
 twelve lines (one for each month) with the calculated temperatures separated by spaces'''

 with open("high_temps.txt", "r") as hTemps
    for line in hTemps:
        