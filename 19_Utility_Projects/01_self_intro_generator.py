"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime

user_name = input("Enter your name: ").strip()
user_age = input("Enter your age: ").strip()
user_city = input("Enter your city: ").strip()
user_profession = input("Enter your profession: ").strip()
user_hobby = input("Enter your favorite hobby: ").strip()


introduction_message = (
    f"Hello! My name is {user_name}. "
    f"I am {user_age} years old and live in {user_city}. "
    f"I work as a {user_profession} and I enjoy {user_hobby} in my free time. "
    f"Nice to meet you!"
)

current_date = datetime.date.today().isoformat()
date_message = f"Logged on: {current_date}"


introduction_message += f"\n {date_message}"
print(introduction_message)

border = "*" * 80
final_output = f"{border}\n{introduction_message}\n{border}"

print(final_output)
