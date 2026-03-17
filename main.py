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
###########  DAY 2   ##########
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

#---------------------------------2ndprogram-----------------------------------------------

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
#-----------------------------------Program 3 Happy Numbers-------------------------

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

def is_happy(num):
    while num != 1 and num != 4:   
        total = 0
        
        while num > 0:
            digit = num % 10
            total += digit * digit
            num = num // 10
        
        num = total
    
    return num == 1


count = 0

for n in numbers:
    if is_happy(n):
        count += 1

print("Total Happy Numbers:", count)

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

#-------------------------------------program 7 no-repeating element-------------------------

numbers = [4, 5, 1, 2, 0, 4, 1, 2]

for num in numbers:
    if numbers.count(num) == 1:
        print("First non-repeating element:", num)
        break
#----------------------------------program  8 min element in list---------------------------

numbers = [1, 5, 7, 3, 2]
print("Minimum element:", min(numbers))

#----------------------------------pogram 10 sub list sum equal to 0---------------------------------

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

 #------------------------------------------------------------------------------------- 
 # Program 1: Filter people under 18 and get remaining names

people = [
    {"name": "Ravi", "age": 22},
    {"name": "Anu", "age": 16},
    {"name": "Kiran", "age": 19},
    {"name": "Meena", "age": 15}
]

adults = list(filter(lambda p: p["age"] >= 18, people))
names = list(map(lambda p: p["name"], adults))

print(names)

#------- Filter Adults And Map Names -------#



# Program 2: Product of all numbers using reduce and lambda

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print(product)

#------- Product Using Reduce -------#



# Program 3: Squares of even numbers using list comprehension and lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

is_even = lambda x: x % 2 == 0

squares = [x**2 for x in numbers if is_even(x)]

print(squares)

#------- Squares Of Even Numbers -------#



# Program 4: Lambda to check if a string is a number

check_number = lambda s: s.isdigit()

print(check_number("123"))
print(check_number("abc"))

#------- Check String Is Number -------#



# Program 5: Extract year, month, day using lambda

from datetime import datetime

date = datetime.now()

extract_date = lambda d: (d.year, d.month, d.day)

print(extract_date(date))

#------- Extract Date Parts -------#



# Program 6: Generate Fibonacci series up to n terms using lambda

fib = lambda n: [0, 1] if n == 2 else [0, 1] + [0]*(n-2)

def fibonacci(n):
    seq = fib(n)
    for i in range(2, n):
        seq[i] = seq[i-1] + seq[i-2]
    return seq[:n]

print(fibonacci(10))

#----------------------------------------------------------------------------------#   
#------- Problem 1 : Bank Account -------#

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   # encapsulation

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print("Interest:", interest)


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount < self.min_balance:
            print("Minimum balance requirement not maintained")
        else:
            super().withdraw(amount)


# Example usage
s = SavingsAccount("101", 1000, 5)
s.deposit(500)
s.withdraw(200)
s.calculate_interest()

c = CurrentAccount("102", 2000, 500)
c.withdraw(1800)


#------- Problem 2 : Employee Management -------#

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass


class RegularEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class ContractEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


# Example usage
e1 = RegularEmployee("John", 30000)
e2 = ContractEmployee("Mike", 120, 200)
e3 = Manager("Sara", 50000, 10000)

print(e1.name, "Salary:", e1.calculate_salary())
print(e2.name, "Salary:", e2.calculate_salary())
print(e3.name, "Salary:", e3.calculate_salary())