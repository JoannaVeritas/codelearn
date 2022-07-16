'''simple hangman game'''

import random
import urllib.request


def gallows(number_of_lives): 
    match number_of_lives:
        case 10:
            return None

        case 8:
            return print('''

|           
|           
|           
|          
|          
|

''')
        case 8:
            return print('''
_____________
|           
|           
|           
|          
|           
|          
|

''')
        case 7:
            return print('''
_____________
|           |
|           |
|           
|          
|           
|          
|

''')
        case 6:
            return print('''
_____________
|           |
|           |
|           O
|          
|           
|          
|

''')
        case 5:
            return print('''
_____________
|           |
|           |
|           O
|           |
|           |
|          
|

''')
        case 4:
            return print('''
_____________
|           |
|           |
|           O
|          /|
|           |
|          
|

''')
        case 3:
            return print('''
_____________
|           |
|           |
|           O
|          /|\\
|           |
|          
|

''')
        case 2:
            return print('''
_____________
|           |
|           |
|           O
|          /|\\
|           |
|          / 
|

''')
        case 1:
            return print('''
_____________
|           |
|           |
|           O
|          /|\\
|           |
|          / \\
|
''')

def wordGenerate():
    '''w tym przypadku wyciagamy slowa z konkretnej strony internetowej, po czym
    dodajac random.choice wybieramy losowe slowo '''
    fhand = urllib.request.urlopen('https://www.randomlists.com/data/words.json')
    #fhand = open('words.txt')
    for data in fhand:
       x = data.decode()
    slowa = x.replace('"', '').split(',')

    # '''otworz plik z dysku i stworz liste slowa'''
    # fhand = open('many_words.txt')
    # czytajPlik = fhand.read()
    # slowa = czytajPlik.split()

    secretWord = random.choice(slowa)
    return secretWord


# list_of_words = ['cat', 'dog', 'mouse', 'elephant']
lives = 9
secret_word = wordGenerate()
guessed_correctly = [] # letters 
not_in_word = []

underscored = list('_' * (len(secret_word))) # whole word as underscores in a list

slowo_jako_lista = list(secret_word)


def welcome():
    print('Welcome to hangman. Your job is to guess the word randomly selected before your 9 lives run out.\n')
    print('Word selected has', len(secret_word), 'letters:', ('_'*len(secret_word) ))

def checking_the_guess():
    guess = input('gimme a letter: ')
    if guess in slowo_jako_lista:
        guessed_correctly.append(guess)
        print('yes,', '"', guess, '"', 'is in my word')
        
        n = 0
        while n < len(secret_word):
            if slowo_jako_lista[n] == guess:
                slowo_jako_lista[n] = '_' # bez tej linijki wpada mi w infinita!! que?
                underscored[n] = guess
                continue
            n += 1

    else:
        print('"',guess, '"', 'is not in the word') 
        not_in_word.append(guess)
        global lives
        gallows(lives)
        print('You have', (lives - 1), 'lives left')
        lives = lives - 1
        
    print('----->',''.join(underscored))


def word_guess():
    print('Do you want to guess the word? If guessed incorrectly you will loose a life. y or n')
    decission = input()

    if decission == 'y' or decission == 'yes':
        print("What's the word?")
        w_guess = input()
        print()
        if w_guess == secret_word:
            print('BRAVO! You guessed correctly. Congratulations')
            exit()
        else:
            print("Nope. You didn't guess correctly my word. You loose a life.")
            global lives
            
            gallows(lives)
            lives = lives - 1
            print('You have', lives, 'lives lefttttttt')

    elif decission == 'n' or decission == 'no':
        print()


def play():
    welcome()
    
    while lives != 0:
        checking_the_guess()
        print('Letters not in my word:', not_in_word)
        # gallows(lives) # to tutaj dalo ciekawa pierwsza loop. anv02.py - que? z terminala vsc?
        # print('You still have', lives, 'lives left')
        word_guess()
    if lives == 0 or lives < 0:
        print('Nicely playes buy you loose. My selected word was:', secret_word)
    

play()


