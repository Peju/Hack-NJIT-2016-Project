import time
import random

openPlz = open('wordbank.txt','r')
readPlz = openPlz.read()
wordBank = readPlz.split()

open2 = open('highscore.txt','r+')
open2lst = open2.readlines()

stat = True
strike = 0
score = 0

def gameMain(wordBank):
    #Primary game loop. Returns a lst:
    #lst[0] = added points, lst[1] = added strikes
    lst = [0,0]
    start = time.time()
    wordQuiz = wordBank[random.randint(0,(len(wordBank)-1))]
    wordType = input('Type the word '+ wordQuiz + ': ')
    if wordType == wordQuiz and time.time()-start < 7:
        lst[0] += 1
    elif time.time()-start >= 7:
        print('STRIKE! Too Slow!')
        lst[1] += 1
    else:
        print('STRIKE! Watch your spelling!')
        lst[1] += 1
    return lst

def highScore(name,score,highScoreLst,zFile):    
    for line in highScoreLst:
        if score >= int(line[-3:-1]): 
            highScoreLst.insert(highScoreLst.index(line),name+'-'+str(score)+'\n')
            highScoreLst.pop()
            zFile.seek(0,0)
            zFile.writelines(highScoreLst)
            break

def rsg():
    print('Ready?')
    time.sleep(1)
    print('Set?')
    time.sleep(1)
    print('Go!')
    time.sleep(1)

name = input('Enter a 3 character ID: ')
print("Type the word then press enter in under 7 seconds!")
time.sleep(2)
rsg()

#MainState

while stat == True:
    lst = gameMain(wordBank)
    score += lst[0]
    strike += lst[1]
    if strike == 3:
        time.sleep(.5)
        print('Game Over!')
        time.sleep(2)
        print('Your Score: ' + str(score))
        highScore(name,score,open2lst,open2)
        time.sleep(2)
        break
print('Highscores')
time.sleep(2)
for line in open2lst:
    print(line, end='')
    time.sleep(1.5)
time.sleep(5)



openPlz.close()
open2.close()

