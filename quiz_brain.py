
# The logic of the game
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        # List of questions
        self.question_list = question_list
        # Score of the quiz
        self.score = 0
        self.current_question = None

    # Get a question
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    # Check if the list contains the next question
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Check the user answer is correct or not
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.increase_score()
            return True
        else:
            return False

    # Increase score
    def increase_score(self):
        self.score += 1
