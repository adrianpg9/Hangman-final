
import random
import hangman_art
import hangman_words





chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



print(hangman_art.logo)



#Create blanks
display = []
guessed_letters = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in guessed_letters:
        guessed_letters.append(guess)

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
          
            print("The letter " + guess + " is not in the word. ")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.\n")
                print("The correct answer is: " + chosen_word)

        #Join all the elements in the list and turn it into a String.
        if end_of_game !=True:
            print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")


        print(hangman_art.stages[lives])
    else:
        print("You already guessed " + guess)
