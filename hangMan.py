import time as t #Only used once lol

def game():
    word = getWord() #Grabs word
    wordArr = [i for i in word] #Splits the word into a char array
    savedNumArr = [] #Used for guessed letter indexs
    lettersGuessed = [] #Saves all the letters that have been guessed
    lives = 3 #What do you think this does, Fool.
    counter = 0 #Because python for loops are stupid and don't use int i values
    correct_guess = False #Yea.
    win = False #Also Yea.

    for i in range(300): #Makes the Console output 300 lines. So you can't see the guess.
        print()

    while True: #No recusion baybee. We while loops 'round here.

        if lives == -1: #Having the lives -1 makes more sense when playing. Get some wrong answers and you'll see why.
            break

        if len(lettersGuessed) == len(wordArr): #If all the letters that have been guessed are in the original word, they musta won.
            win = True
            break

        guess = input("Guess letter: ").lower() #literally doesn't work if you input more than one char. I'm not doing it either cuz I hate python.

        if inArr(wordArr, guess) and not inArr(savedNumArr, wordArr.index(guess)): #Checks to see if the word has been guessed already, and then saves the index of the letter, and the letter itself.
            savedNumArr.append(wordArr.index(guess))
            correct_guess = True

            for i in wordArr: #This has to be a for loop because of reacurring letters in words
                if guess == i:
                    lettersGuessed.append(i)
            
        if inArr(wordArr, guess): #If the letter has already been guessed, it's still a correct guess, but the information already exists in the arrays.
            correct_guess = True
        else:
            print("Lives Remaining: " + str(lives)) #If neither one of the If catch it. A live is taken away.
            lives = lives - 1

        for i in wordArr: #Prints the letters and dashes. 
            if inArr(lettersGuessed, i):
                print(i, end = '')
            elif inArr(savedNumArr, counter) and correct_guess == True:
                print(wordArr[counter], end = '')
            else:
                print("-", end = '')
            counter = counter + 1

        correct_guess = False   # 
        counter = 0             # These reset the things that need to be reset.
        print()                 #
    
    winLoss(win)

def winLoss(win): #Yea
    if win:
        print("You won!")
    else:
        print("You lose!")
    t.sleep(100)
            
def getWord(): #Also yea
    return input("What word: ").lower()


def inArr(array, var_to_find): #Checks to see if the value appears in an array. Probably built in already but I couldn't find it.
    for i in array:
        if i == var_to_find:
            return True


game()
