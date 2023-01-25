import random
import os

def passSpcCharacters():
    char_list = ['!','*','#','_','^','%','&','@','$']
    spc_string = str()
    iter_var = 0
    while iter_var < 4:
        spc_string += str(random.choice(char_list))
        iter_var+=1
    return spc_string
       
def  passBaseString():
    with open('random_text.txt','r') as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        
    base_string = random.choice(words)
    if len(base_string) > 4:
        ''.join(random.sample(base_string, len(base_string)))
        base_string = base_string[0:4]
        ''.join(random.choice((str.upper, str.lower))(char) for char in base_string)
        return base_string
    elif len(base_string) < 4:
        passBaseString()
    
def passNumElements():
    idealNum = random.randint(12345,98706)
    return idealNum
        
def Generator():
    baseWord = passBaseString()
    baseNum = str(passNumElements())
    baseSpcChars = passSpcCharacters()
    
    initPassword = baseWord + baseNum + baseSpcChars
    
    finalPassword = ''.join(random.sample(initPassword, len(initPassword)))
    ''.join(random.sample(finalPassword, len(finalPassword)))
    
    return finalPassword

    

