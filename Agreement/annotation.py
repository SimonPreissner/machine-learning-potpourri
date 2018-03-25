'''Collect annotation from human subject.'''

import random

classes = [1,2,3,4,5]

def read_questions():
    f = open("data/questions.txt")
    questions = f.readlines()
    return questions

def write_annotation(username, answers):
    f = open("annotations/"+username+".txt",'w')
    for k,v in answers.items():
        f.write(k.rstrip('\n')+"::"+str(v)+"\n")
    f.close()

questions = read_questions()
random.shuffle(questions)
answers = {}

username = input("Please enter your name: ")

print("Now, answer each question with a value (1-5). You can always quit by pressing 'q'.\n\n")

for q in questions:
    user_answer = input(q)
    while user_answer not in [str(c) for c in classes] and user_answer != 'q':
        user_answer = input("Please enter a value in the range (1-5)\n"+q)
    if user_answer == 'q':
        break
    else:
        answers[q] = user_answer

write_annotation(username,answers)
print("Thank you! Your annotations are in the file annotations/"+username+".txt")
