"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400
  Neha owes ₹400
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

try:
    # Handle number of people input
    while True:
        try:
            number_of_people = int(
                input("Enter the number of people in the group: ").strip()
            )
            if number_of_people <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a whole number for the group size.")

    person_names = []

    for person_index in range(1, number_of_people + 1):
        person_name = input(f"Enter the name of person {person_index}: ").strip()
        person_names.append(person_name)

    # Handle total bill input
    while True:
        try:
            total_bill_amount = float(input("Enter the total bill amount: ").strip())
            if total_bill_amount < 0:
                print("The bill cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value for the bill.")

    # Calculate split
    bill_per_person = total_bill_amount / number_of_people

    print("\n" + "=" * 35)
    print("        BILL SUMMARY")
    print("=" * 35)

    print(f"Total bill amount : ₹{total_bill_amount:.2f}")
    print(f"Number of people  : {number_of_people}")
    print(f"Amount per person : ₹{bill_per_person:.2f}")

    print("-" * 35)

    for person_name in person_names:
        print(f"{person_name} owes ₹{bill_per_person:.2f}")

    print("=" * 35)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
