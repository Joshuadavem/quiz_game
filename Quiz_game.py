## Quiz game

import random 

print("Welcome to the quiz game! Try and answer these questions to the best of your ability.")

quiz = {
    "What is the capital city of Japan?":"Tokyo",
    "What is the smallest country in the world?":"Vatican city",            #The questions for the quiz
    "What two countries share the largest border?":"Canada and America",
    "What is 5 x 5 + 10?":"35",
    "What language do they speak in Mexico?":"Spanish"
}

quiz_contents = list(quiz.items())              #Puts the questions in random order
random.shuffle(quiz_contents)

score = 0

for question, answer in quiz_contents:
    print(question)
    user_answer = input("Your answer: ")
    if user_answer == answer or user_answer.lower() == answer.lower():   # Plays through the game, gives you questions, and you put an answer
        print("Correct!")
        score += 1
    else: 
        print(f'Incorrect... the answer was {answer}')


print(f'Your final score is: {score} out of {len(quiz)}')  #Final score of the quiz

if score < 1:
        print('Did you even try?')
elif score > 1 and score < 3:
        print('I mean... its not zero I guess')
elif score > 2 and score < 4:
        print('Not bad! you pass!')                             #Gives you a little comment based on your score
elif score > 3 and score < 5:
        print('Wow that a performance!!! Well done.')
elif score == 5: 
        print('PERFECT SCORE!!')

