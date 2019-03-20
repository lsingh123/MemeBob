from random import *
def Meme (phrase):
    x = len(phrase)
    randomNumbers=[]
    for y in range (0,int(x/2)):
        randomNumbers.append(randint(0,x))
    i=0
    for d in range (0,x):
        if i in randomNumbers:
            phrase=phrase[0:i]+phrase[i].upper()+phrase[i+1:]
        i=i+1
    return phrase
        
            
