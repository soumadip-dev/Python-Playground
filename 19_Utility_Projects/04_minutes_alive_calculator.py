"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""


def calculate_age_in_time(age_in_years):

    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = age_in_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR

    return round(total_days), round(total_hours), round(total_minutes)


while True:
    try:
        age_in_years = float(input("Enter your age in years: "))

        total_days, total_hours, total_minutes = calculate_age_in_time(age_in_years)

        print("\nYou are approximately:")
        print(f"- {total_days:,} days old")
        print(f"- {total_hours:,} hours old")
        print(f"- {total_minutes:,} minutes old")

        try_again = input("\nWould you like to try again? (y/n): ").strip().lower()

        if try_again != "y":
            print("Goodbye.")
            break

    except ValueError:
        print("Please enter a valid number for age.")
