import random

def read_words_from_file(file_path):
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return words

word_list = read_words_from_file("words.txt")

if not word_list:
    raise ValueError("The word list is empty. Please ensure the file contains words.")

word = word_list[random.randint(0, len(word_list) - 1)]
current_attempt = ["_" for _ in word]

print(" ".join(current_attempt))
print("Welcome to Hangman! You will be given 10 attempts to guess the correct word\n"
      "The word is randomly chosen from a list\n"
      "You may guess one character at a time")

guessed_letters = []
wrong_guesses = 0
finished = False

def user_guess(guess, word, current_attempt, guessed_letters, wrong_guesses):
    if not guess.islower():
        return f"Invalid input. Please enter a lowercase letter.", False, wrong_guesses
    
    if len(guess) > 1:
        return f"Invalid input. Please enter a single lowercase letter", False, wrong_guesses
    
    if guess in guessed_letters:
        return f"You have already entered this letter. Try again, please.", False, wrong_guesses
    else:
        guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        if wrong_guesses > 9:
            return f"You have lost!\nThe word was {word}!\nPlease try again!", True, wrong_guesses
        return (f"That letter is not in the word. You have {10 - wrong_guesses} attempts left\n"
                f"You have previously guessed {guessed_letters}\n"
                f"You have got {' '.join(current_attempt)} so far"), False, wrong_guesses

    for idx, letter in enumerate(word):
        if letter == guess:
            current_attempt[idx] = guess

    if "_" not in current_attempt:
        return (f"You have won!\n"
                f"You correctly guessed the word was {word}\n"
                f"You had {10 - wrong_guesses} attempts remaining!"), True, wrong_guesses
    return (f"That is correct, {guess} was in the word\n"
            f"This is what you have so far {' '.join(current_attempt)}\n"
            f"You have {10 - wrong_guesses} attempts remaining"), False, wrong_guesses

while not finished:
    guess = input("Please enter the letter you would like to guess: ")
    message, finished, wrong_guesses = user_guess(guess, word, current_attempt, guessed_letters, wrong_guesses)
    print(message)
