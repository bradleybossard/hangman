import random

def draw_hangman(count):
    print('')
    if count > 0:
        print(' O ')
    if count > 1:
        print('/', end="")
    if count > 2:
        print(' \\')
    if count > 3:
        print(' |')
    if count > 4:
        print('/', end="")
    if count > 5:
        print(' \\')
    print('')

words = ['automobile', 'airplane', 'exhausted']

word = random.choice(words)

guesses = []
guess_count = 0

while True:
    print('Whats you guess')
    guess = input ()
    guesses.append(guess)
    if guess not in word:
        guess_count = guess_count + 1
    draw_hangman(guess_count)
    if guess_count == 6:
        print('You\'ve been hanged')
        break;

    did_win = True
    for w in word:
        if w in guesses:
            print(w, end="")
        else:
            did_win = False
            print('+', end="")
    print('')
    if did_win:
        print('You won!')
        break;
