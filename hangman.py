# Simple Python Hangman created by https://github.com/kevintr303 under The MIT License
# Uses RazorSh4rk's random word api https://github.com/RazorSh4rk/random-word-api
import json
import random

use_api = False

with open("words.json", "r") as f:
    words = json.loads(f.read())


def generate_random_word():
    if not use_api:
        random_word = random.choice(words["data"])
        random_word = random_word.replace("-", " ")
        random_word = [x for x in random_word]
        return random_word
    else:
        import requests
        r = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        random_word = r.text
        return random_word


def start_game():
    already_guessed = []
    random_word = generate_random_word()
    guesses = ""
    while not guesses.isdigit():
        guesses = input("Input difficulty (number of lives): ")
        if guesses == "0":
            guesses = ""
    guesses = int(guesses)
    print("Start guessing!")
    hidden = ["_" if x != " " else " " for x in random_word]
    while guesses > 0:
        print("".join(hidden))
        guess = input()
        if guess in already_guessed:
            print("Already guessed", guess)
            continue
        already_guessed.append(guess)
        if guess in random_word:
            indices = [index for index, element in enumerate(random_word) if element == guess]
            for index in indices:
                hidden[index] = guess
        else:
            guesses -= 1
        if guess == "".join(random_word):
            print("".join(random_word))
            print("You got it! Congratulations!")
            return
        print("You have", guesses, "guesses left")
        if hidden.count("_") == 0:
            break
    if guesses == 0:
        print('You lost. The word was:', "".join(random_word))
        return
    else:
        print('You got it! Congratulations!')
        return


if __name__ == "__main__":
    print("Welcome to Hangman")
    while True:
        start_game()
        play_again = None
        while play_again not in ['yes', 'y', 'no', 'n']:
            play_again = input("Do you want to play again? [yes/no]\n").lower()
            if play_again in ['yes', 'y']:
                continue
            else:
                print("Goodbye.")
                import sys
                sys.exit()
        continue
