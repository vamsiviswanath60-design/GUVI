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
#  DAY 2#
#-------------------------------1st pragram-------------------------
given_list = [10, 501 , 22 , 37 , 100 ,999 ,87 , 351]

Even_Number_list = []
Odd_Number_list =[]

for num in given_list:
    if num % 2==0 :
        Even_Number_list.append(num)
    else :
        Odd_Number_list.append(num)

print("even list:",  Even_Number_list)        
print("Odd list:", Odd_Number_list)

#----------------2ndprogram--------------------------------------------

given_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_list = []

for num in given_list:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)

print("Prime numbers are:", prime_list)
print("Count of prime numbers:", len(prime_list))

#-----------------------------------program 4 sum of firist and last digit ------------------------------------------

num = int(input("Enter a number: "))

last_digit = num % 10

while num >= 10:
    num = num // 10

first_digit = num

print("Sum of first and last digit:", first_digit + last_digit)

#------------------------------------program 5 no of ways coins ----------------------------------------
count = 0

for one in range(11):          
 for two in range(6):       
  for five in range(3):  
   for ten in range(2):  

    total = (one * 1) + (two * 2) + (five * 5) + (ten * 10)

    if total == 10:
     print("1₹:", one, 
        "2₹:", two, 
        "5₹:", five, 
        "10₹:", ten)
    count += 1

print("\nTotal number of ways:", count)

#------------------------------------program 6 duplicates-----------------

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 3]

duplicates = []

for num in list1:
    if num in list2 and num in list3:
        duplicates.append(num)

print("Duplicate elements:", duplicates)

#-------------------------------------program 7 no-repeating element------------

numbers = [4, 5, 1, 2, 0, 4, 1, 2]

for num in numbers:
    if numbers.count(num) == 1:
        print("First non-repeating element:", num)
        break
#----------------------------------program  8 min element in list-------------

numbers = [1, 5, 7, 3, 2]
print("Minimum element:", min(numbers))

#----------------------------------pogram 10 sub list sum equal to 0     ----------------------------

numbers = [4, 2, -3, 1, 6]

found = False

for i in range(len(numbers)):
    total = 0
    
    for j in range(i, len(numbers)):
        total += numbers[j]
        
        if total == 0:
            print("Sub-list with sum 0 found")
            found = True
            break
    
    if found:
        break

if not found:
    print("No sub-list with sum 0")

 #---------------------------------------END-------------------------------------   
     