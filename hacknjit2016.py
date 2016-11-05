import time
import random

openPlz = ('wordbank.txt',"r")
readPlz = openPlz.read()
wordBank = readPlz.split()

stat = true
strike = 0
score = 0

def gameMain(wordBank):
    #Primary game loop. Returns a lst:
    #lst[0] = added points, lst[1] = added strikes
    lst = [0,0]
    start = time.time()
    while time.time()-start < 7:
        wordQuiz = wordBank[random.randint(0,len(wordBank))]
        wordType = input('Type the word '+ wordQuiz)
    if wordType == wordQuiz:
        lst[0] += 1
    else:
        lst[1] += 1
    return lst    

print("Type the word then press enter!")

while stat == true:
    lst = gameMain(wordBank)
    score += lst[0]
    strike += lst[1]
    if strike == 3:
        break

print('Game Over!')
print('Your Score: ' + str(score))


openPlz.close()
