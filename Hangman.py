import random
A = ['h', 'a','n', 'g', 'm','a','n']
L = ['_', '_', '_', '_','_','_','_']
Words = 'apple', 'tree', 'beach', 'pinapple', 'adventure', 'happy', 'travel'
  
Words = Words.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
Word = random.choice(Words)   
play = True
strikes = 0

while play == True:
    # Check if all letters guessed
    if Word == L:
        print('You win!')
        break
    # Ask the user to guess a letter
    if strikes < 6:
        # Check if the user has less than 6 strikes, if they do they can guess
        letter = str(input('Guess a letter: '))

        i = 0
        # guessed is true if the user gets at least one letter
        guessed = False
        for currentLetter in A:
            if letter == currentLetter:
                Word[i] = letter
                # Prints what the user has so far
                print(' '.join(str(n) for n in L))
                guessed = True
        # if last index and bad guess
            elif i == (len(Word)-1) and not guessed:
                print('Bad Guess!')
                stikes += 1 # increment strike by 1
                print('Strike ' + str(strikes))
        
        i += 1 # increment to next letter in A
    else:
        print('You lose!')
        break

print("Great Job!")

    