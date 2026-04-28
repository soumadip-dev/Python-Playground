questions_list = [
    [
        "What does JS stand for?",
        "Java Syntax",
        "JavaScript",
        "Just Script",
        "Jumbo Script",
        2,
    ],
    [
        "Which company developed JavaScript?",
        "Microsoft",
        "Google",
        "Netscape",
        "Apple",
        3,
    ],
    [
        "Which keyword is used to declare a variable in JavaScript?",
        "var",
        "int",
        "string",
        "define",
        1,
    ],
    [
        "Which method is used to print in Python?",
        "console.log()",
        "echo()",
        "print()",
        "printf()",
        3,
    ],
    [
        "What is the file extension for Python files?",
        ".pt",
        ".py",
        ".pyt",
        ".python",
        2,
    ],
    [
        "Which hook is used for state in React?",
        "useFetch",
        "useState",
        "useData",
        "useEffect",
        2,
    ],
    [
        "Which hook runs side effects in React?",
        "useState",
        "useEffect",
        "useReducer",
        "useRef",
        2,
    ],
    [
        "What is Node.js?",
        "Frontend framework",
        "Database",
        "JavaScript runtime",
        "CSS library",
        3,
    ],
    [
        "Which module is used to create a server in Node.js?",
        "http",
        "fs",
        "url",
        "path",
        1,
    ],
    [
        "Which keyword is used for async functions in JavaScript?",
        "await",
        "async",
        "defer",
        "promise",
        2,
    ],
    [
        "Which data type is immutable in Python?",
        "List",
        "Dictionary",
        "Set",
        "Tuple",
        4,
    ],
]


# Prize money for each correct answer
prize_list = [
    100000,
    320000,
    400000,
    450000,
    500000,
    1000000,
    2000000,
    3000000,
    4000000,
    5000000,
    6000000,
]


current_question_index = 0
total_earnings = 0


# Loop through each question
for question_data in questions_list:

    # Display question and options
    print("\n" + question_data[0])
    print(f"a. {question_data[1]}")
    print(f"b. {question_data[2]}")
    print(f"c. {question_data[3]}")
    print(f"d. {question_data[4]}")

    # Take user input
    user_answer = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))

    # Validate input
    if user_answer < 1 or user_answer > 4:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    # Check if the answer is correct
    correct_answer = question_data[5]

    if user_answer == correct_answer:
        print("Correct answer.")

        total_earnings += prize_list[current_question_index]
        current_question_index += 1

    else:
        print(f"Incorrect answer. The correct option was {correct_answer}.")
        print("Game over. Better luck next time.")
        break


print(f"\nTotal prize money won: ₹{total_earnings}")
