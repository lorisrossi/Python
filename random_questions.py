# This Python file uses the following encoding: latin-1
# Utilizzo: Modifica la stringa 'questions' per avere domande a random
import random, time

questions = """Fill here your text.
Each line correspond to a question.
You can use these sentences to try this code.
Enjoy!!""".splitlines()

random.seed()
command = 'something'
while (command != 'n'):
    print(random.choice(questions))
    time.sleep(2) #stops for 2 seconds
    #print ''
    command = raw_input("Continue? Type 'n' to stop.")
    print ''
