import random
a = ["Trashcan", "Car", "Sunset", "Tree"]
b = ["hits", "likes", "hates", "watches"]
c = ["you", "them", "me", "her"]
lst = [a, b, c]
def rndm():
    rslt = ""
    for i in range(0,3):
        rndm_in = random.randint(0,3)
        rslt = rslt + lst[i][rndm_in] + " "
    return rslt
print(rndm())