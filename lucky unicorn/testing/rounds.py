balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...")
while play_again == "":


    #increase # of rounds rounds_played
    rounds_played += 1

    # Print round number
    print(rounds_played)
    balance -= 1
    print("balance: ", balance)
    print()


    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("press Enter to play play again "
      "or 'xxx' to quit")


print()
print("Final balance", balance)