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
        if score >= int(line[-2:]): 
            lst.insert(lst.index(line),name+'-'+str(score))
            lst.pop()
            zFile.seek(0,0)
            zFile.writelines(lst)

def rsg():
    print('Ready?')
    time.sleep(1)
    print('Set?')
    time.sleep(1)
    print('Go!')
    time.sleep(1)


print("Type the word then press enter in under 7 seconds!")
time.sleep(3)
rsg()

while stat == True:
    name = input('Enter a 3 character ID')
    lst = gameMain(wordBank)
    score += lst[0]
    strike += lst[1]
    if strike == 3:
        print('Game Over!')
        print('Your Score: ' + str(score))
        highScore(name,score,open2lst)
        break
print('Highscores')
for line in open2lst:
    print(line)
    time.sleep(1.5)
        



openPlz.close()
open2.close()
'''


    
'''
<<<<<<< HEAD
=======

>>>>>>> origin/master
