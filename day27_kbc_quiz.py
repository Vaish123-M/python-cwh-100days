"""
# Day 27: Exercise 3 - Kaun Banega Crorepati (KBC)

Create a console quiz using lists or tuples for questions, options, correct
answers, and prize amounts.  Each question has four options labeled A-D.
The player wins the prize for a correct answer; the game ends on the first
wrong answer.

The quiz reads each answer with `input()` and normalizes it with
`.strip().upper()`.
"""

questions = (
    ("Which language is this course about?", ("A. Java", "B. Python", "C. C", "D. Go"), "B", 1000),
    ("What is 2 + 2?", ("A. 3", "B. 4", "C. 5", "D. 6"), "B", 2000),
    ("Which keyword defines a function?", ("A. def", "B. func", "C. function", "D. make"), "A", 5000),
)


def play_quiz():
    """Run the interactive quiz and return the total prize."""
    winnings = 0
    for question, options, correct_answer, prize in questions:
        print("\n" + question)
        print(" | ".join(options))
        answer = input("Your answer (A-D): ").strip().upper()
        if answer == correct_answer:
            winnings += prize
            print("Correct! Current winnings:", winnings)
        else:
            print("Incorrect. The correct answer was", correct_answer)
            break
    return winnings


print("Final prize:", play_quiz())
