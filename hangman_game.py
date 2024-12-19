import random #importing random module for randomly choosing a word

from hangman_stages import hangman_stages # importing the hangman stages from the hangman_stages.py file

limits =6 # setting the limits of the game to 6

words_list = ["carrot","banana","pineapple","beetroot","rose"] # list of words to be chosen randomly
chosen_word = random.choice(words_list) # choosing a random word from the list

display_empty =[] #the letters of the word will be displayed as underscores/ like empty list
for i in range(len(chosen_word)): #for loop to iterate through the chosen word to store empty spaces in the display_empty list
    display_empty.append("_")
print(display_empty)

game_over = False # game_over as false to end game when the game is over
while not game_over: # while loop to keep the game running until the game is over
    guessed_letter = input("guess a letter: ").lower() # taking input from the user to guess a letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter: # if the guessed letter is in the chosen word then the letter will be displayed in the display_empty list
            display_empty[position] = letter
    print(display_empty)
    
    # checking is all the spaces are filled with letters then the game is over
    if "_" not in display_empty:
        game_over = True
        print("you won the game...")
        
        # checking if the guessed letter is not in the chosen word then the limit will be decreased by 1 which will be displayed on the screen with hangman stages
    if guessed_letter not in chosen_word:
        limits -=1
        print(hangman_stages[6-limits]) # displaying the hangman stages
        print("you have " +str(limits)+" left")
        if limits == 0:
            game_over = True
            
            print("you lost the game...")

            

