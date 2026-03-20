"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

emoji_dictionary = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}


user_message = input("Enter your message: ").strip()

updated_word_list = []

for word in user_message.split():

    cleaned_word = word.lower().strip(".,!?")

    emoji_symbol = emoji_dictionary.get(cleaned_word, "")

    if emoji_symbol:
        updated_word_list.append(f"{word} {emoji_symbol}")
    else:
        updated_word_list.append(word)


enhanced_message = " ".join(updated_word_list)

print("\nEnhanced message:\n")
print(enhanced_message)




