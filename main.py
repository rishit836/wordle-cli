import random

with open("words.txt") as f:
    data = f.readlines()
    for index,word in enumerate(data):
        data[index] = word.strip()

print("""=========================================
           WELCOME TO WORDLE           
=========================================
Objective: Guess the hidden 5-letter word.
You have 5 attempts.

INSTRUCTIONS:
1. Each guess must be a VALID word from the dictionary.
2. Each guess must be EXACTLY 5 letters long.

HOW TO READ YOUR RESULTS:
After each valid guess, the word will be reprinted using the following code:
  • UPPERCASE  : The letter is in the word AND in the correct position.
  • lowercase  : The letter is in the word BUT in the wrong position.
  • Underscore : The letter is NOT in the word at all.

-----------------------------------------
EXAMPLE SCENARIO
Target Word: GHOST
Your Guess : THOSE

Result     : t h O S _

Explanation:
 't' is lowercase (Exists in GHOST, but wrong position).
 'h' is lowercase (Exists in GHOST, but wrong position).
 'O' is UPPERCASE (Exists in GHOST, and correct position).
 'S' is UPPERCASE (Exists in GHOST, and correct position).
 '_' is underscore (The letter 'E' does not exist in GHOST).
-----------------------------------------

""")

start = input("Press ENTER to continue...")

chances = 5
word = random.choice(data)
while chances>0:

    print(word)
    guess = input("Guess a Word: ")
    if len(guess) != 5:
        print("Enter a 5 letter word!")
        continue
    else:
        # checking if the entered word is valid vocab or not
        # if guess in data:
        chances -=1

        for index,letter in enumerate(guess):
            if letter == word[index]:
                print(letter,end=" ")
            elif letter in word[index:]:
                print(letter.upper(),end=" ")
            else:
                print("_",end=" ")
        print()


