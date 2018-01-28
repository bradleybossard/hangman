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

for i in range(7):
    draw_hangman(i)
