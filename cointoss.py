import random

flips = 0
heads = 0
tails = 0

while flips < 5000:
    headtail = random.randint(1, 2)

    if headtail == 1:
        heads = heads + 1
        print "Throwing a coin...It's a head!...Got", heads, "heads so far and", tails, "so far"
    if headtail == 2:
        tails = tails + 1
        print "Throwing a coin...It's a tail!...Got", heads, "heads so far and", tails, "so far"
    flips = flips + 1
