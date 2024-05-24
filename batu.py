import random

def number_guessing() :
    generated_number=random.randint(1,10)
    attempts=0
    while True :
     try :
        guess= int(input("type the guessed number : "))
        break
     except ValueError as e :
        print(f"please enter an integer: {e}")
    while generated_number != guess :
        print(f"try again")
        attempts=attempts + 1
        if generated_number > guess:
            print(f"try a bigger number")
            while True :
             try :
                guess=int(input("new guessed number : "))
                break
             except ValueError as e :
                print(f"please enter an integer: {e}")
        elif generated_number < guess: 
            print(f"try a smaller number")
            while True :
               try :
                guess=int(input("new guessed number : "))
                break
               except ValueError as e :
                  print(f"please enter an integer: {e}")
    
        
    print(f"right! after" + " " + str(attempts + 1)+ " " + "attempts")
    again = input("press 1 if you want to play again")
    cleaned_again = again.strip()
    if cleaned_again == "1" :
        number_guessing()
    
number_guessing()

