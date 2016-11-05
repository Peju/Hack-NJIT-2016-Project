import time
import random


openPlz = ('wordbank.txt',"r")
readPlz = openPlz.read()

wordBank = readPlz.split()

#JJ
strike = 0
score = 0
print("Type the word then press enter!")
while time.time()-start < 7:
    start = time.time()
    wordQuiz = wordBank[random.randint(0,len(wordBank))]
    wordType = input('Type the word '+ wordQuiz)
    if wordType == wordQuiz:
        score += 1
        continue
    strike += 1
    if strike == 3:
        print('Game Over!')
        print('Your Score: ' + str(score))
        break
