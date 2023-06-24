from data import question_data
from question_model import *
from quiz_brain import *
question_bank = []
for item in question_data["results"]:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

quiz.end_quiz()