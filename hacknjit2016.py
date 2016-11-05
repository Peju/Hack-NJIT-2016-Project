import time
import random


openPlz = (wordbank.txt,"r")
readPlz = openPlz.read()

wordBank = readPlz.split()

#JJ
stat = true
strike = 0
score = 0
print("Type the word then press enter!")
while stat == true:
    start = time.time()
    while time.time()-start < 7:
        wordQuiz = wordBank[random.randint(0,len(wordBank))]
        wordType = input(wordQuiz)
        if wordType == wordQuiz:
            score += 1
            continue
        else:
            strike += 1
    strike += 1
    if strike == 3:
            print('Game Over!')
            break
