secret_number = 9

guessing = 0
guess_limit = 3

while guessing < guess_limit:
    guess = int(input("Guess: "))
    guessing += 1


    if secret_number == guess:
        print("You won!")
        break

else:
    print("You lost, Try again!")


