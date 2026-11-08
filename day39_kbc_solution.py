"""
# Day 39: Exercise 3 - KBC Solution

This clean KBC solution stores each question, options, answer, and prize in
one tuple.  The game stops at the first incorrect answer and returns the
player's winnings.  Prepared answers keep this example runnable without
interactive input.
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


def play_quiz_with_answers(answers):
    """Run a quiz using a fresh iterator for each question."""
    answer_stream = iter(answers)
    winnings = 0
    for question, options, correct_answer, prize in QUESTIONS:
        print("\n" + question)
        print(" | ".join(options))
        answer = next(answer_stream, "").strip().upper()
        if answer != correct_answer:
            print("Incorrect. The correct answer was", correct_answer)
            break
        winnings += prize
        print("Correct! Current winnings:", winnings)
    return winnings


print("Final prize:", play_quiz_with_answers(["b", "B", "A"]))
print("Prize after wrong answer:", play_quiz_with_answers(["B", "C", "A"]))
