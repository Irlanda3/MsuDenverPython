from random import randint, seed
debug =True

#numero de veces como que agitamos una bolsa
seed(73)

names = ["Scotty","Michelle","Kelly","Aaron","Laura","Kyle","James","Henc","Anayeli"]

#list of givers is also the list of receivers
receivers = names.copy()

#create an empty list for the matches
matches = []

for giver in names:
    #copy the original list
    givers = names.copy()

    #remove the person giving the gift
    givers.remove(giver)

    #finf the intersection between the set of givers and receivers
    candidates = [name for name in receivers if name in givers]

    #randomly choose a receiver from the set of candidates
    receiver = candidates[randint(0, len(candidates)-1)]

    if debug:
        print("giver: ", giver)
        print("givers: ", givers)
        print("receivers: ", receivers)
        print("candidates: ", candidates)
        print("receiver: ", receiver)

        #create the match
        matches.append((giver, receiver))
        
        # remove the person who already is getting a gift
        receivers.remove(receiver)

print(matches)