import random

def passSpcCharacters():
    char_list = ['!','*','#','_','^','%','&','@','$']
    spc_string = str()
    iter_var = 4
    
    #! Selecting (4) Random Special Characters
    while iter_var:
        spc_string += str(random.choice(char_list))
        iter_var-=1
    return spc_string
       
def  passBaseString():
    #! Opening Text File "random_text.txt" and acessing letters for password
    with open('random_text.txt','r') as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        
    base_string = random.choice(words)
    
    #! Randomizing / Shuffling the base word
    ''.join(random.sample(base_string, len(base_string)))
    base_string = base_string[0:4]
    
    #! Randomizing the Case of the characters
    ''.join(random.choice((str.upper, str.lower))(char) for char in base_string)
    return base_string
    
def passNumElements():
    #! Selecting random digits 
    idealNum = random.randint(12345,98706)
    return str(idealNum)
        
def Generator():
    baseWord = passBaseString()
    baseNum = passNumElements()
    baseSpcChars = passSpcCharacters()
    
    #! Creating initial Password String
    initPassword = baseWord + baseNum + baseSpcChars
    
    #! Randomizing again to return final password
    finalPassword = ''.join(random.sample(initPassword, len(initPassword)))
    ''.join(random.sample(finalPassword, len(finalPassword)))
    
    return finalPassword

    

