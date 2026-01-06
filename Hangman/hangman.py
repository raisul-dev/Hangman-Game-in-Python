import random
words = {
    "animals":["cat","dog","elephant","tiger","lion"],
    "countries":["bangladesh","india","japan","usa","uk"],
    "fruits":["apple","banana","mango","orange","grapes"]
}
def hangman():
    category =random.choice(list(words.keys()))
    word = random.choice(words[category])
    word_list = list(word)
    guessed=["_"]*len(word)
    lives = 6
    print(f"Category:{category}")
    print("".join(guessed))
    
    while "_" in guessed and lives>0:
        guess = input("Guess a letter:").lower()

        if guess in word:
            for i,letter in enumerate (word_list):
                if letter==guess:
                    guessed[i]=guess
            print("".join(guessed))
        else:
            lives -= 1
            print(f"Worng!Lives left:{lives}")
            print("".join(guessed))
    if"_" not in guessed:
        print("You won!The word was:",word)
    else:
        print("Game over!The word was:",word)

#paly the game ......
hangman()