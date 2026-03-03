import random
#-----------------------------------program 1 Guess the Number#----------------------------------------------------------------
Number_to_guess = random.randint(1,5)

while True :
    Gamer_guess = int (input("Gamer guess pls enter a  num to win lottery :" ))
    if Gamer_guess > Number_to_guess:
       print ("Guessed wrong try smaller num for your party")
    elif Gamer_guess < Number_to_guess:
       print ("Guessed wrong try bigger num for you party")
    else :
       print("won 500000 CRORES Congrats congrats")
       break

#-----------------------------------program 2 Guess the scrambled words #---------------------------------------------------------

words = ['python', 'javascript', 'selenium', 'pytest' , 'guvi' , 'automation' , 'java']

original_word = random.choice(words)
letters = list(original_word)
random.shuffle(letters)

scrambled = ""
for ch in letters: scrambled += ch    
print("Scrambled word:", scrambled)

while True:
    guess = input("Enter your guess: ")

    if guess == original_word:
        print("Correct! 🎉")
        break
    else:
        print("Wrong guess. Try again!")

#-------------------------------------------------------------------------------------------------#        