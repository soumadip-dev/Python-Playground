user_age = int(input("Enter your age: "))

if user_age > 18:
    print("You are eligible to drive.")
    print("Thank you.")
elif user_age == 18:
    print("You are eligible to apply for a driving licence.")
else:
    print("You are not eligible to drive yet.")
    print("Sorry.")
