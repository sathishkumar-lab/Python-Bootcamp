import random
from hangman_art import stages,logo

lives=6
print(logo)

word_list = ["mango","orange","kiwi"]

chosen_word=random.choice(word_list)
#print(chosen_word)

#To find "_" for chosen_word
placeholders=""
wordlength=len(chosen_word)
for position in range (wordlength):
    placeholders+="_"
print(placeholders)

gameover=False

#Create a empty list to store the guessed letters
corrected_letters=[]

#Use while to continue the game untill gameover
while not gameover:
    
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess=input("Guess the letter : ").lower()

    if guess in corrected_letters:
        print(f"you've already guessed {guess}")

    #check each letter in the words by guess
    display=""
    for letter in chosen_word:
        if letter in guess:
            display+=letter
            corrected_letters.append(guess)
        elif letter in corrected_letters:
            display+=letter
        else:
            display+="_"
    print(display)

    

    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        if lives==0:
            gameover=True
            print(f"*********************** YOU LOSE **********************")

    if "_" not in display:
        gameover=True
        print(f"*********************** YOU WIN **********************")

    print(stages[lives])
