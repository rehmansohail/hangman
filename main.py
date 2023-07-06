import random
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6


print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while display.count("_")!=0:
  if lives==0:
    print("You lost")
    print(hangman_art.stages[0])
    break
  print(*display)
  guess = input("Guess a letter: ").lower()
  if display.count(guess)!=0:
    print("You already guessed this letter dummy, try again")
    continue
  if chosen_word.find(guess) !=-1:
    for position in range(word_length):
      letter = chosen_word[position]
    
      if letter == guess:
        display[position] = letter
  
  else:
    print(hangman_art.stages[lives])
    lives-=1
    
  

if lives !=0:
  print("You won")