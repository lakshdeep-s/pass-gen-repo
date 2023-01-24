from pass_generator import Generator

def relaunchApp():
    runAgain = input("would you like to generate another password ? : (Y/N) : ").lower()
    if runAgain == 'y':
        passwordGenerator()
    elif runAgain == 'n':
        print("See you later then !!")

def welcomeMessage():
    print("Hello There welcome to the password generator !!")
    print("This Generator will generate a secure password using python !!")


def passwordGenerator():
    # welcome messages
    welcomeMessage()
    # generate password
    generatedPassword = Generator()
    
    print(f"Your Password is : {generatedPassword}")
        
    relaunchApp() 

passwordGenerator()   
        
    
    
    