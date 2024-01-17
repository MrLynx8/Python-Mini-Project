import random

# Defining a list of questions and their answers
questions = [
    {
        "question": "What is Python?",
        "options": [
            "A large snake",
            "A high-level programming language",
            "A type of web browser",
            "A tropical fruit"
        ],
        "correct_answer": "A high-level programming language"
    },

    {
        "question": "What symbol is used for comments in Python?",
        "options": [
            "#",
            "//",
            "--",
            "/* */"
        ],
        "correct_answer": "#"
    },
    {
        "question": "Which statement is used to exit a loop prematurely in Python?",
        "options": [
            "break",
            "exit",
            "return",
            "end"
        ],
        "correct_answer": "break"
    },
    {
        "question": "What does the 'print' function do in Python?",
        "options": [
            "Pause the program",
            "Display output on the screen",
            "Delete a file",
            "Create a new variable"
        ],
        "correct_answer": "Display output on the screen"
    },
    {
    "question": "Which keyword is used to define a function in Python?",
    "options": ["define", "function", "def", "fun"],
    "correct_answer": "def"
    },
    {
    "question": "What is the result of 3 + 4 * 2 in Python?",
    "options": ["10", "14", "11", "8"],
    "correct_answer": "11"
    },
    {
    "question": "How do you create a list in Python?",
    "options": ["list = [1, 2, 3]", "set = {1, 2, 3}", "tuple = (1, 2, 3)", "array = [1, 2, 3]"],
    "correct_answer": "list = [1, 2, 3]"
    },
    {
    "question": "Which of the following data structures in Python is mutable?",
    "options": ["List", "Tuple", "String", "Set"],
    "correct_answer": "List"
    },
    {
    "question": "Which of the following is NOT a valid Python variable name?",
    "options": ["my_var", "123var", "_var", "var123"],
    "correct_answer": "123var"
    },
    {
    "question": "What is the purpose of the 'elif' keyword in Python?",
    "options": ["It defines a new function", "It checks for exceptions", "It is used in    a for loop", "It adds an alternative condition in an if-else statement"],
    "correct_answer": "It adds an alternative condition in an if-else statement"
    }
]


# Shuffling the questions to randomize their order
random.shuffle(questions)

# Initializing a variable to keep track of the player's score
score = 0

# Iterating through the questions and ask them one by one
for index, question_data in enumerate(questions, start=1):
    print(f"Question {index}: {question_data['question']}")
    for i, option in enumerate(question_data['options'], start=1):
        print(f"{i}. {option}")

    # Getting player's answer
    player_answer = input("Enter the number of your answer: ")

    # Checking if the player's answer is correct
    if player_answer.isdigit() and 1 <= int(player_answer) <= len(question_data['options']):
        player_answer = question_data['options'][int(player_answer) - 1]
        if player_answer == question_data['correct_answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question_data['correct_answer']}\n")
    else:
        print("Invalid input. Please enter the number corresponding to your answer.\n")

# Displaying the player's final score
print(f"You got {score} out of {len(questions)} questions correct.")
