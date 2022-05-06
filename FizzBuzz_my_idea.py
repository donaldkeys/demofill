for number in range(1, 51):
    print(number)

    while number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        break

    if number % 3 == 0:
        print("fizz")

    elif number % 5 == 0:
        print("Buzz")

    #else:
        #pass

