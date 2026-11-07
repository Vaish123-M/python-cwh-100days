"""
# Day 27: Exercise 3 - Kaun Banega Crorepati (KBC)

Create a console quiz using lists or tuples for questions, options, correct
answers, and prize amounts.  Each question has four options labeled A-D.
The player wins the prize for a correct answer; the game ends on the first
wrong answer.

This runnable example uses a prepared answer list so it can be validated
without interactive input.  A real console version could replace that list
with `input()` and normalize answers with `.strip().upper()`.
"""

questions = (
    ("Which language is this course about?", ("A. Java", "B. Python", "C. C", "D. Go"), "B", 1000),
    ("What is 2 + 2?", ("A. 3", "B. 4", "C. 5", "D. 6"), "B", 2000),
    ("Which keyword defines a function?", ("A. def", "B. func", "C. function", "D. make"), "A", 5000),
)


def play_quiz(answers):
    """Run the quiz with supplied answers and return the total prize."""
    winnings = 0
    for question, options, correct_answer, prize in questions:
        print("\n" + question)
        print(" | ".join(options))
        answer = answers.pop(0).strip().upper() if answers else ""
        if answer == correct_answer:
            winnings += prize
            print("Correct! Current winnings:", winnings)
        else:
            print("Incorrect. The correct answer was", correct_answer)
            break
    return winnings


# A copy protects the caller's original answers from pop().
sample_answers = ["b", "B", "A"]
print("Final prize:", play_quiz(sample_answers.copy()))

# Empty input is treated as incorrect rather than crashing.
print("Prize after empty answers:", play_quiz([]))
