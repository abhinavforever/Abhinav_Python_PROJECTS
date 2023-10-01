from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    i_text=i["question"]
    i_answer=i["correct_answer"]
    new_q=Question(text=i_text,answer=i_answer)  
    question_bank.append(new_q)
# for j in question_bank:
#     print(j.text,j.answer)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")
