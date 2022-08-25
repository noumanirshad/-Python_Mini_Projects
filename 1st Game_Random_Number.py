import random
rand = random.randint(1,100)
guesses = 0
user = True
while user != rand:
    user = int(input("Enter the number between 0 to 100: "))
    if(user < rand):
        print("Please enter larger number: ")
    elif(user > rand):
        print("Please enter smaller number: ")
    else: 
        print(f"your number of guesss: {guesses+1}")
    guesses = guesses + 1
with open("HighScore.txt", 'r') as f:
    r = f.read()
if r == '' or int(r)>(guesses):
    with open("HighScore.txt", "w") as e:
        e.write(str(guesses))
        print("\t\tCongratulations, \nYou are master mind:\n\tYou have created new High Score:  ", guesses)
