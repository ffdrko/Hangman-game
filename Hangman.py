import random as r
from hangman_word import word_list as wl

computer_choice = r.choice(wl)
word_length = len(computer_choice)
print(f"The length of the word is {word_length}")

# print(computer_choice)

end_game = False
lives = 6

from hangman_art import logo

print(logo)


display = []
for _ in range(word_length):
    display += "_"

# print(display)

while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = computer_choice[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if guess not in computer_choice:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")
            print(f"The word made you crazy  was {computer_choice}")
    if "_" not in display:
        end_game = True
        print("You win.")
    from hangman_art import stages

    print(stages[lives])