from data import question_data
from question_model import *
from quiz_brain import *
from ui import QuizInterface
import html


# The main
def main():
    question_bank = []
    for item in question_data:
        question_bank.append(Question(html.unescape(item["question"]), item["correct_answer"]))

    quiz = QuizBrain(question_bank)
    gui = QuizInterface(quiz)

    while quiz.still_has_questions():
        quiz.next_question()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
