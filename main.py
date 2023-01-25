from pass_generator import Generator

def relaunchApp():
    runAgain = input("would you like to generate another password ? : (Y/N) : ").lower()
    if runAgain == 'y':
        passwordGenerator()
    elif runAgain == 'n':
        print("\nSee you later then !!")
    else:
        print("\nSorry I dont understand...Try again maybe...\n")
        relaunchApp()

def welcomeMessage():
    print("----------------------\nHello There welcome to the password generator !!")
    print("This Generator will generate a secure password using python !!\n----------------------\n")


welcomeMessage()
def passwordGenerator():
    
    generatedPassword = Generator()
    
    print(f"\n---*---*---*---*--\nYour Password is : {generatedPassword}\n---*---*---*---*--")
        
    relaunchApp() 

passwordGenerator()   
        
    
    
    