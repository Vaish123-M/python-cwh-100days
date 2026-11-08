"""
# Day 39: Exercise 3 - KBC Solution

This clean KBC solution stores each question, options, answer, and prize in
one tuple.  The game stops at the first incorrect answer and returns the
player's winnings.  Answers are read interactively with `input()`.
"""

QUESTIONS = (
    (
        "Which language is this course about?",
        ("A. Java", "B. Python", "C. C", "D. Go"),
        "B",
        1000,
    ),
    (
        "What is 2 + 2?",
        ("A. 3", "B. 4", "C. 5", "D. 6"),
        "B",
        2000,
    ),
    (
        "Which keyword defines a function?",
        ("A. def", "B. func", "C. function", "D. make"),
        "A",
        5000,
    ),
)


def play_quiz():
    """Run the interactive quiz."""
    winnings = 0
    for question, options, correct_answer, prize in QUESTIONS:
        print("\n" + question)
        print(" | ".join(options))
        answer = input("Your answer (A-D): ").strip().upper()
        if answer != correct_answer:
            print("Incorrect. The correct answer was", correct_answer)
            break
        winnings += prize
        print("Correct! Current winnings:", winnings)
    return winnings


print("Final prize:", play_quiz())
