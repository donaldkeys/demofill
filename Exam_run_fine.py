sales = int(input("Enter number of sale(s) : "))

message1 = f" You earned £{1000 + 250 } Great job, Keep it up!"
message2 = f"You have {10 - sales} sale(s) Shortage(s)"
message3 = f" You earned £{1000} Pounds\n You could earn more by putting in an etra effort!"

while sales >= 11:
    print(message1)
    break

if sales < 10:
    print(message2)

if sales == 0:
    print("You get nothing!")

elif sales == 10:
    print(message3)
else:
    pass







