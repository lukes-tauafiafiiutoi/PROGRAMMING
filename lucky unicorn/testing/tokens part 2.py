import random

# main
tokens =["unicorn", "horse", "zebra", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

# testing loop
for item in range(0,20):
    chosen = random.choice(tokens)


    #Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5    





