"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer
  💡 Making things beautiful
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

import textwrap

user_name = input("Enter your name: ").strip()
user_profession = input("Enter your profession: ").strip()
user_passion = input("Enter your one-line passion or goal: ").strip()
favorite_emoji = input("Enter your favorite emoji (optional): ").strip()
website_handle = input("Enter your website or social handle (optional): ").strip()

print("\nChoose your bio style:")
print("1. Simple layout")
print("2. Vertical style")
print("3. Emoji border style")

selected_style = input("Enter your choice (1/2/3): ").strip()


def generate_bio(style_choice):

    if style_choice == "1":
        return (
            f"{favorite_emoji} {user_name} | {user_profession}\n"
            f"💡 {user_passion}\n"
            f"🔗 {website_handle}"
        )

    elif style_choice == "2":
        return (
            f"{favorite_emoji} {user_name}\n"
            f"💼 {user_profession}\n"
            f"🔥 {user_passion}\n"
            f"🔗 {website_handle}"
        )

    elif style_choice == "3":
        return (
            f"{favorite_emoji * 3}\n"
            f"{user_name} - {user_profession}\n"
            f"{user_passion}\n"
            f"{website_handle}\n"
            f"{favorite_emoji * 3}"
        )

    else:
        return "Invalid style selection. Please choose 1, 2, or 3."


generated_bio = generate_bio(selected_style)


print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(generated_bio))
print("*" * 50)


save_option = input("Do you want to save this bio to a text file? (y/n): ").lower()


if save_option == "y":

    file_name = user_name.lower().replace(" ", "_") + "_bio.txt"

    with open(file_name, "w", encoding="utf-8") as file_handle:
        file_handle.write(generated_bio)

    print("The bio has been saved successfully.")
