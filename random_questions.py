# python encoding: latin-1
# How-to-use: read the string 'questions' and modify it

import random, time

questions = """Fill here your text.
Each line correspond to a question.
You can use these sentences to try this code.
Enjoy!!""".splitlines()

random.shuffle(questions)
N = len(questions)
for i in range(N):
    print i+1, "/", N
    print questions[i]
    time.sleep(2) #stops for 2 seconds
    command = raw_input("Continue? Type 'n' to stop.")
    if command == 'n':
        break
    print

print
print "Congratulations!! Well done!"
