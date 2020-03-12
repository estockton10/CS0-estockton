"""
Assignment-Guess the number game
This file lets user guess a number between 1 and 20 in 6 attempts
CSCI 110
By- Emily Stockton
"""
 
  
   
import random 
number = random.randint(1, 20) 
##CHANGE TO 1,20!!!!

  
def guess_number(): 
    print("Welcome to guess a number game!")
    name=input("What is your name?") 
    print("Hello",name)
    print("Guess a number (between 1 and 20), you have 6 attempts:") 
    chances = 0 
    while chances < 6: 
        
        # Enter a number between 1 to 20 
        guess = int(input()) 
        
        
        if guess == number: 
            
            print("Congratulations", name)
            print("You win!!!")
            print("You guessed the number in",chances,end=" "),
            print("tries")
            break
            
        
        elif guess < number: 
            print("Your guess was too low: Guess a number higher than", guess) 
    
                    
        else: 
            print("Your guess was too high: Guess a number lower than", guess) 
            
        
        chances += 1
            
    if not chances < 6: 
        print("Sorry, you loose. The number is", number) 


def main():
    #count=0
    while True:
        #global count
        guess_number()
        #count+=1

        answer = input("Would you like to play again? [Y|N]")
        if answer == 'y':
            continue
        elif answer=='Y':
            continue
        else:
            break
    print
#print (count)

main()

