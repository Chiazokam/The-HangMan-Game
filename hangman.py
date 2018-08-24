# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    counter = 0
    #code below added here by me...

     #lambda expression to change  word in list to lower case
    lower_case_word =[x.lower() for x in letters_guessed ]
    #transverse through the loop to check if it is in the secret word
    for i in lower_case_word:
        if i in secret_word:
           # if char == i:
          counter +=1
          #print(counter)


    #check if the length of secret_word  matches counter number
    if counter==len(secret_word):
        return True
    else :
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
     #counter
    counter = 0
    #code below added here by me...
    #temp_data_list=list(secret_word[:])
    temp_data_list=["_ "] * len(secret_word)
    che_data_list =[]
    #print(secret_word)
    #transverse through the loop to check if it is in the secret word
    for (i,val) in enumerate(letters_guessed):
        if val in secret_word:
            #check if how many times the word is in the temporary data list.
            if val in che_data_list:
                 counter +=1

            else:
           # add the word in a temporary data structure.

             counter +=1

            num_data_list =[i  for i,v in enumerate(secret_word) if v==val]
            #go the length and add it and the right position
            for num in num_data_list:
                 temp_data_list[num] = val

            #add to the che_data_list
            che_data_list.append(val)
        #else :
           #adding the default underscore
           #temp_data_list[i] = "_ "
         #  print("hey")


    #check if the length of secret_word  matches counter number
    if counter==len(secret_word):
        return "".join(temp_data_list)
    else :
        #return print("Hey sorry player no such word exist in the secret word.wrong guess")
        return "".join(temp_data_list)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
# =============================================================================
#     all_alphabets = string.ascii_lowercase
# 
#     not_letters_guessed = ""
#     
#     for letter in all_alphabets:
#         
#         if letter not in letters_guessed:
#             
#             not_letters_guessed += letter
#             
#     return not_letters_guessed
# =============================================================================  
    #Better codes
    available_letters = string.ascii_lowercase
    
    for letter in letters_guessed:
        
        available_letters = available_letters.replace(letter, "")
        
    return available_letters

#==============================================================================
#FUNCTION TO TEST THE USER'S INPUT IN THE HANGMAN GAME
#==============================================================================
    
def user_input_requirements():

    warning = 0
    
    users_guess_history = []
    
    while warning < 3:
        
        users_guess = input("Make a guess. Put in a letter: ").lower()
        
        if users_guess not in "abcdefghijklmnopqrstuvwxyz":
            
            print("You can only put in an alphabet")
            
            warning += 1
            
        elif users_guess == "":
            
            print("You must guess an alphabet")
           
        else:
            return users_guess

#==============================================================================
#FUNCTION TO STOP USER FROM REPEATING GUESSES            
#==============================================================================
            
def guess_non_repeat(users_guess, letters_guessed):
    
    if users_guess in letters_guessed:
        
        #letters_guessed.remove(users_guess)
        
        print("You have made this guess already!")
        
#==============================================================================
#FUNCTION TO RETURN THE COUNT OF UNIQUE LETTERS IN THE SECRET WORD          
#==============================================================================                

def count_unique_letters(secret_word):
     
    return len(set(secret_word))

#==============================================================================
#FUNCTION TO REDUCE GUESSING CHANCES IF WRONG GUESS IS A VOWEL OR CONSONANT          
#==============================================================================

def reduce_guess(users_guess, num_of_guesses_left):
    
    if users_guess in "aeiou":
        
        num_of_guesses_left -= 2
        
    else:
        
        num_of_guesses_left -= 1
        
    return num_of_guesses_left
#==============================================================================
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print("Welcome to the Hangman game!")
    
    #Variable conatining the random word chosen by the computer. For testing
    secret_word = choose_word(wordlist)
    
    #For testing
    print(secret_word)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    
    print("I am thinking of a word that is", str(len(secret_word)), "letters long")
    
   # print(guessed_words)
    
    #Initializing the list containing all the guessed letters
    letters_guessed = []
    
    print("                                                  ")
    #print("You have", str(num_of_guesses_left), "guesses left")
    
    print("Available Letters:", get_available_letters(letters_guessed))
    
    num_of_guesses_left = 6
    
    while num_of_guesses_left >= 0:
    
        #Take in the user's guess with the user_input_requirement function
        users_guess = user_input_requirements()
        
        letters_guessed.append(users_guess)
        
        #guess_non_repeat(users_guess, letters_guessed)
        
        
        #Check if the guessed letter is in the computer's chosen word
        if users_guess in secret_word:
            
            #letters_guessed.append(users_guess)
            
            #guess_non_repeat(users_guess, letters_guessed)
            
            print("You have", str(num_of_guesses_left), "guesses left")
            
            print(letters_guessed)
            
            print("Available Letters:", get_available_letters(letters_guessed))
            
            print("Good Guess:", get_guessed_word(secret_word, letters_guessed ))         
                     
            print("__________________________________________")
            
            if get_guessed_word(secret_word, letters_guessed ) == secret_word:
                
                print("                                          ")
                
                total_score = num_of_guesses_left * count_unique_letters(secret_word)
                
                print("Your total score is:", str(total_score))
                
                print("                                          ")
                
                print("Congratulations!!!")
                
                break
            
        else:
            
            #guess_non_repeat(users_guess, letters_guessed)
            
            print(letters_guessed)
            
            num_of_guesses_left = reduce_guess(users_guess, num_of_guesses_left)
            
            print("Available Letters:", get_available_letters(letters_guessed))
            
            print("You have", str(num_of_guesses_left), "guess(es) left")
            
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed ) )
            
            print("__________________________________________")
            
            
            if num_of_guesses_left == 0:
                
                print("                                          ")
                
                print("Sorry dude, you've run out of guesses!!")
                
                print("                                          ")
                
                print("The Word is:", secret_word.upper())
                
                print("                                          ")
                
                print("Game Over!!!")
                
                break
            



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
