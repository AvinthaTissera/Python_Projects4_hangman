import random

from hangman_art import stages

from hangman_words import word_list

#Select a word from a word list 
chosen_word = random.choice(word_list)

end_of_game = False

#Create a variable called 'lives' to keep track of the number of lives left
#Set 'lives' to eqaul 6
lives = 6

from hangman_art import logo
print(logo)

#TESTING
#print(f'Psst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display += "_"


#input users guesses and looping through
while not end_of_game: 
    guess= input("Guess :").lower()

    #check the letter if the user has already entered
    if guess in display:
        print(f"You already guessed {guess} letter.")


    #check for guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    #if guess is not correct, then reduce the lives by 1
    #if lives down to 0 then guesser loose.
    if guess not in chosen_word:
        print(f"You have guessed {guess}, thats not in the word. You loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose.")

    #joing all the elements in the list and turn into a String
    print(f"{' '.join(display)}")

    # Check if user has got all the letters 
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    #print the ASCII art according to remaining lives
    
    print(stages[lives])



