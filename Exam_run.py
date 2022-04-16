sales = int(input("Sales made: "))

shortage = (10 - sales)
weekly_payment = 1000


if sales >= 10:

    print(f"£{1000 + 250}")
    print("You did well, Great job!")

elif sales < 10:

    print(f"You have {shortage} shortage(s)")
    print

else:
    print(f"{weekly_payment} Pounds")

