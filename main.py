import os
import random
from feedback import get_feedback
os.chdir(os.path.dirname(os.path.abspath(__file__)))

currentAvail=[]
fullAvail=[]

with open("wds.txt","r") as db:
    for line in db:
        fullAvail.append(line[0:5])

currentAvail=fullAvail


print("To play, enter 6 five-letter words. After each word, you will get feedback about each letter in that word.\n\t(2): This letter is correct and in the correct place.\n\t(1): This letter is correct but in the wrong place.\n\t(0): this letter is not in the 'correct' word at all.")

for trie in range(6):
    fail=True
    inp=""
    while fail:
        inp=input("Enter a 5 letter word below:\n\t").lower()
        if len(inp) != 5 or not inp.isalpha():
            print("Words must all be 5 letters, and not use any other symbols!")
            continue
        if inp in fullAvail:
            fail=False
        else:
            print("This is not a valid 5 letter word. Please try again!")


    resultList=[]
    length=0
    for word in currentAvail:
        if word==inp:
            continue
        length+=1
        resultList.append(get_feedback(word,inp))

    if length==0:
        status="22222"
        print("You win!")
        break
    else:
        status=max(set(resultList), key=resultList.count)

    print("\t"+status)
    #print(length)

    temp=[]

    length=0
    for word in currentAvail:
        result=get_feedback(word,inp)
        if result==status:
            temp.append(word)
            length+=1
    currentAvail=temp
    print(length,"possible words remain")




try:
    print("The correct answer was:\n\t"+random.choice(currentAvail))#print the actual answer that was definitely locked in all along
    print("=================\n\n\nOther possible remaining options:")
    print(currentAvail)
except:
    pass
