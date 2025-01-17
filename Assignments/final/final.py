"""
Final Project
this program lets user play a game of hangman
CSCI 110
Date- 27 April 2020
Author- Emily Stockton

"""

#Select difficulty code makes program crash...
"""
def select_difficulty():
    difficulty = input(''' Select a difficulty level from below... 
    (E) for words between 3 and 5 letters 
    (M) for words between 5 and 7 letters 
    (H) for words 7 letters and longer 
    (A) for all words of all length 
     ''').upper()

    valid_difficulty = False 
    if 'E' in difficulty: 
        valid_difficulty = True 
        lengthMin = 3 
        lengthMax = 5 

    if 'M' in difficulty: 
        valid_difficulty = True 
        lengthMin = 5 
        lengthMax = 7 

    if 'H' in difficulty: 
        valid_difficulty = True 
        lengthMin = 7 
        lengthMax = sys.maxsize 

    if 'A' in difficulty: 
        valid_difficulty = True 
        lengthMin = 3 
        lengthMax = sys.maxsize 
            
    if len(difficulty)>1: 
        valid_difficulty = False 
    if valid_difficulty is False:
        print('Input error') 
        return select_difficulty() 
    return [lengthMin, lengthMax]


length_limit=select_difficulty()
length_min=length_limit[0]
length_max=length_limit[1]
word=wordList[int(random.random()*len(wordList))].upper()

while len(word)<length_min or len(word)>length_max:
    word=wordList[int(random.random()*len(wordList))].upper()
"""

import sys
import random
import string

#welcome player to game
print("Welcome to hangman!" )
name=input("What is your name?")
print("Hello",name)
print("The computer will pick a random word for you to guess. Start by guessing a letter")
print("If you guess all of the letters, you win!")


#get words from txt file
wordList=open('words.txt','r').readlines()
wordList=[word.strip() for word in wordList]

#generate random word
def get_word():
    global word, hidden, wrong_guesses
    word=wordList[int(random.random()*len(wordList))].upper()

    word= list(word)
    hidden=''
    for char in word:
        hidden+='_'
    hidden=list(hidden)

    wrong_guesses = []



#function prints if player correctly gueesed word or not
def end_of_game(winner):
    print('\n')
    if winner:
        print('You win! You guessed the word correctly! The word was ' +''.join(word))
    else:
        print('You lose. You did not guess the word correctly. The word was ' +''.join(word))
            
            
#function shows player's correct and incorrect guesses and number of guesses and determines if player eneter a valid guess 
def guess_word():
    print('WORD: ' + ' '.join(hidden))
    print('Wrong guesses ('+str(len(wrong_guesses))+'): ' + ' '.join(wrong_guesses))
    guess = input('GUESS: ').upper()
    valid_guess=True

    if guess not in string.ascii_uppercase or len (guess)!=1:
        valid_guess=False
        print('You have entered an invalid letter')
        guess_word()

    if guess in wrong_guesses or guess in hidden:
        valid_guess=False
        print('You have already guessed that letter')
        guess_word()  
        
    correct_index=[]

    for index in range (len(word)):
        if word [index] == guess:
            correct_index.append(index)
    if guess not in word and valid_guess:
        wrong_guesses.append(guess)
    for index in correct_index:
        hidden[index]=guess


#function prints gallows for each incorrect guess
def gallows():
    if len(wrong_guesses)==0:
        print('|__________ '  )                      
        print('|/         |') 
        print('|    ')  
        print('|') 
        print('|   ')   
        print('|') 
        print('|   ')                             
        print('-------------')

    if len(wrong_guesses)==1:
        print('|__________ '  )                      
        print('|/         |') 
        print('|          0')  
        print('|           ' )
        print('|          ')
        print('|         ' )  
        print('|') 
        print('|   ')                             
        print('-------------')

    if len(wrong_guesses)==2:
        print('|__________ '  )                      
        print('|/         |') 
        print('|          0')  
        print('|          | ' )
        print('|           ')
        print('|           ' )  
        print('|') 
        print('|   ')                             
        print('-------------')

    if len(wrong_guesses)==3:
        print('|__________ '  )                      
        print('|/         |') 
        print('|          0')  
        print('|         /|  ' )
        print('|           ' )  
        print('|') 
        print('|   ')                             
        print('-------------')

    if len(wrong_guesses)==4:
        print('|__________ '  )                      
        print('|/         |') 
        print('|          0')  
        print('|         /|\\  ' )
        print('|           ' )  
        print('|') 
        print('|   ')                             
        print('-------------')

    if len(wrong_guesses)==5:
        print('|__________ '  )                      
        print('|/         |') 
        print('|          0')  
        print('|         /|\\  ' )
        print('|         /   ' )  
        print('|') 
        print('|   ')                             
        print('-------------')

    if len(wrong_guesses)==6:
        print('|__________ '  )                      
        print('|/         |') 
        print('|          0')  
        print('|         /|\\  ' )
        print('|         / \\  ' )  
        print('|') 
        print('|   ')                             
        print('-------------') 


#function defines gameplay
def game():
    while True:
        gallows()
        if len(wrong_guesses)>5:
            end_of_game(False)
            break 
        elif '_' not in hidden:
            end_of_game(True)
            break
        guess_word()
        

#main function
def main():
   
    while True:
      get_word()
    
      game()
      
      answer = input("Would you like to play again? [Y|N]")
      if answer == 'y':
          continue
      elif answer=='Y':
          continue
      else:
          break
    

main()
