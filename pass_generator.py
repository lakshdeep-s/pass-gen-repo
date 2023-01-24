import random
import os
from stat import S_IREAD

# making random.txt file readonly
os.chmod("random_text.txt", S_IREAD)

def idelSpcCharacters():
    charList = ['!','*','#','_','^','%','&','@','$']
    spcString = str()
    iterVar = 0
    while iterVar < 4:
        spcString += str(random.choice(charList))
        iterVar+=1
    return spcString
       
def  idealBase():
    with open('random_text.txt','r') as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        
    baseWord = random.choice(words)
    if len(baseWord) > 4:
        ''.join(random.sample(baseWord, len(baseWord)))
        baseWord = baseWord[0:4]
        ''.join(random.choice((str.upper, str.lower))(char) for char in baseWord)
        return baseWord
    elif len(baseWord) < 4:
        idealBase()
    
def idealRandRange():
    idealNum = random.randint(12345,98706)
    return idealNum
        
def Generator():
    baseWord = idealBase()
    baseNum = str(idealRandRange())
    baseSpcChars = idelSpcCharacters()
    
    initPassword = baseWord + baseNum + baseSpcChars
    
    finalPassword = ''.join(random.sample(initPassword, len(initPassword)))
    ''.join(random.sample(finalPassword, len(finalPassword)))
    
    return finalPassword

    

