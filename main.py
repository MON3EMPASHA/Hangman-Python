import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
display = []
for letter in chosen_word:
  display.append("_")

complete_game = True
lives = 7
while complete_game:
  guess = input("Guess a letter: ").lower()
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, thats not in the word. you lose a life.")
  if guess in display:
    print(f"You have already guessed {guess}")
  for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
      display[i] = guess
      
  print(hangman_art.stages[lives])
  print(" ".join(display))
  print("____________________________________________________\n")
  if lives == 0:
    complete_game = False
    print("You Lose")
  if "_" not in display:
    complete_game = False
    print("You Win")
