user_input = int(input("Enter a number:"))
if user_input < 0: 
    print("it's negative")
elif user_input%2 == 0:
    print("It's event")
else:
    print("It's odd")
