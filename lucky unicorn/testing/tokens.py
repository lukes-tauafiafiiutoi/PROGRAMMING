import random

# main
tokens =["unicorn", "horse", "zebra", "donkey"]
balance = 100

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





