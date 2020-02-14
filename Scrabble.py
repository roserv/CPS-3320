Scrabble = {'A': 1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':5, 'G':2, 'H':4, 'I':1, 'J':8, 'K': 5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

def letterScore(letter=0): 
    return Scrabble.get(letter.upper(), 0)

def wordScore(word = input('Please enter a word ')):
    score = 0
    for char in word:
        score = score + letterScore(letter = char)
   
    print('Your score is ' + str(score))   

wordScore()