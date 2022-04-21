sales = int(input("Sales made: "))

shortage = (10 - sales)
weekly_payment = 1000

# For_those_that met the target.
if sales >= 11:
    print(f"You earned £{1000 + 250}\n You did well, Great job!")

if sales == 0:
    print("You get nothing!")

# For_those_that didn't meet the target.
elif sales < 10:
    print(f"You have {shortage} shortage(s), you earned £{(shortage) * 100} ")

# For_those_that had a regular task with no extra or less.
else:
    print(f" You earned £{weekly_payment} \n You can do better, if you put in more effort!")
