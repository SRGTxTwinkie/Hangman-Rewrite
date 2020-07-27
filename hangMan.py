import time as t

def game():
    word = getWord()
    wordArr = [i for i in word]
    savedNumArr = []
    lettersGuessed = []
    lives = 3
    counter = 0
    correct_guess = False
    win = False

    for i in range(300):
        print()

    while True:

        if lives == -1:
            break

        if len(lettersGuessed) == len(wordArr):
            win = True
            break

        guess = input("Guess letter: ").lower()

        if inArr(wordArr, guess) and not inArr(savedNumArr, wordArr.index(guess)):
            savedNumArr.append(wordArr.index(guess))
            correct_guess = True
            for i in wordArr:
                if guess == i:
                    lettersGuessed.append(i)
            
        if inArr(wordArr, guess):
            correct_guess = True
        else:
            print("Lives Remaining: " + str(lives))
            lives = lives - 1

        for i in wordArr:
            if inArr(lettersGuessed, i):
                print(i, end = '')
            elif inArr(savedNumArr, counter) and correct_guess == True:
                print(wordArr[counter], end = '')
            else:
                print("-", end = '')
            counter = counter + 1

        correct_guess = False
        counter = 0
        print()
    
    winLoss(win)

def winLoss(win):
    if win:
        print("You won!")
    else:
        print("You lose!")
    t.sleep(100)
            
def getWord():
    return input("What word: ").lower()


def inArr(array, var_to_find):
    for i in array:
        if i == var_to_find:
            return True


game()
