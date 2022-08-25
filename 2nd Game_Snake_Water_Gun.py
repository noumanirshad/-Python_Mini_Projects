import random
def gamewin(a, b):
    if a == b:
        return None 
    elif (a == "s"):
        if (b == "w"):
            return False
        else:
            return True
    elif (a == "w"):
        if (b == "g"):
            return False
        else:
            return True
    elif (a == "g"):
        if (b == "w"):
            return False
        else:
            return True
rand = random.randint(1,3)
if rand == 1:
    com = "s"
elif rand == 2:
    com = "w"
elif rand == 3:
    com = "g"
print("Computer choosed:  snake(s), water(w), gun(g): " )
you = input("You enter(s, w, g):  snake(s), water(w), gun(g): ")
print("\nYou choose a " , (you))
print("Computer choose a " , (com))

a = gamewin(com, you)
if a == None:
    print("\nYour match have been tie ")
elif a:
    print ("\nCongratulations: you win")
else:
    print("\nYou loose: Next try")
