#1oo days of code
#day 3
#-----------------------------------------------------
#odd or even


# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if(number%2==0):
 print("This number is even")
else:
  print("The number is odd")

#-----------------------------------------------------

#bmi calculator 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi=float(weight)/float(height*height)
bmi1=float(bmi)


if(bmi1<18.5):
 print(f"Your BMI is {bmi1}, you are underweight.")
elif(bmi1<25):
 print(f"Your BMI is {bmi1}, you have a normal weight.") 
elif(bmi1<35):
 print(f"Your BMI is {bmi1}, you are slightly overweight.") 
elif(bmi>=35):
 print(f"Your BMI is {bmi1}, you are clinically obese.") 

#-----------------------------------------------------
 #Leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year%4==0 :
  if year%100==0:
    if year%400==0:
     print("The year is a leapyear")
    else:
     print("The year is not a leap year") 
  else:
   print("The year is  a leapyear")   
else:
  print("The year is not a leap year")   


#----------------------------------------------------------
#PIZZA BILL


# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if(size=='S'):
  if int(add_pepperoni=="Y") & int(extra_cheese=="Y"):
   print(f"Your final bill is: ${18}.")
  elif int(add_pepperoni=="Y") & int(extra_cheese=="N"):
   print(f"Your final bill is: ${17}.") 
  elif int(add_pepperoni=="N") & int(extra_cheese=="Y"):
   print(f"Your final bill is: ${16}.")  
  else:
    print("invalid input") 
if(size=='M'):
  if int(add_pepperoni=="Y") & int(extra_cheese=="Y"):
   print(f"Your final bill is: ${24}.")
  elif int(add_pepperoni=="Y") & int(extra_cheese=="N"):
   print(f"Your final bill is: ${23}.") 
  elif int(add_pepperoni=="N") & int(extra_cheese=="Y"):
   print(f"Your final bill is: ${21}.")  
  else:
    print("invalid input")     
if(size=='L'):
  if int(add_pepperoni=="Y") & int(extra_cheese=="Y"):
   print(f"Your final bill is: ${29}.")
  elif int(add_pepperoni=="Y") & int(extra_cheese=="N"):
   print(f"Your final bill is: ${28}.") 
  elif int(add_pepperoni=="N") & int(extra_cheese=="Y"):
   print(f"Your final bill is: ${26}.")  
  else:
    print("invalid input") 

#----------------------------------------------------------------------------
#LOVE CALCULATOR


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name3 = input("What is your name? \n")
name4 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name3.lower()
name2=name4.lower()
t=int(name1.count("t"))+int(name2.count("t"))
r=int(name1.count("r"))+int(name2.count("r"))
u=int(name1.count("u"))+int(name2.count("u"))
e=int(name1.count("e"))+int(name2.count("e"))
l=int(name1.count("l"))+int(name2.count("l"))
o=int(name1.count("o"))+int(name2.count("o"))
v=int(name1.count("v"))+int(name2.count("v"))

L=l+v+e+o
T=t+r+u+e

print(f"{T}{L}%")
#----------------------------------------------------------------------------------

#TREASURES

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choise=input("left or right")
if choise=="left":
    choise1=input("here is a pond, are you going to wait or you want to swim")
    if choise1=="wait":
      choise2=input("choose the color of the door ypu want to open-RED BLUE OR GREEN")
      if choise2=="blue":
        print("HUU YAA..!YPU FIND THE TREASURES...CONGRAJULATIONS..")
      else:
        print("Your choise is wrong ..GAME OVER") 
    else:
      print("You are  attcached..Game over")
else:
  print("Game over...you fall into the hole")  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#DAY 4
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#Genarating random Heads or tails

import random
a=random.randint(0,2)
if a==0:
  print("Tails")
else:
  print("Heads")  

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#random name to pay the pay the bill

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
b=len(names)
number=random.randint(0,b)
print(f"Finally the {names[number]} need to pay the bill")
#--------------------------------------------------------------------------------------------------
#pirate using nested list

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#--------------------------------------------------------------------------------------------------

#rock paper and scissor


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a=int(random.randint(0,3))
user=int(input("Enter your choice:0 for stone,1 for paper,2 for sciccors"))
if(a==user):
  print("Draw")
elif a==0 and user>0:
  print("computer wins")
elif a==1 and user==0 :
  print("computer wins")
elif a==2 and user==1:
  print("Computer wins")
elif user>2 or user<0:
  print("Invalid input")
else:
  print("you win")        
#------------------------------------------------------------------
#DAY 5
#-----------------------------------------------------------------
#Find average height of students without using inbuild functions

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)

#--------------------------------------------------------------------------
#Max mark of student

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score=0
for score in student_scores:
 if score>highest_score:
  max=score
print(max)    
#------------------------------------------------------------------------
#print sum of even numbers

#Write your code below this row 👇
sum1=0
for i in range(2,101,2):
 sum1 += i
print(sum1) 
#-------------------------------------------------------------------------

#Fizz_Buzz


#Write your code below this row 👇
for i in range(0,100,1):
 if i%3==0 and i%5==0:
   print("Fizz_Buzz")
 elif i%3==0:
   print("Fizz")
 elif i%5==0:
   print("Buzz")
 else:
   print(i)     
#----------------------------------------------------------------------

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
b=""
a=''
c=''
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=''
for i in range(1,nr_letters+1):
  random_char=random.choice(letters)
  a+= random_char

for i in range(1,nr_symbols+1):
  random_sym=random.choice(symbols)
  b+= random_sym

for i in range(1,nr_numbers+1):
  random_num=random.choice(numbers)
  c+= random_num
print(a+b+c)

#-------------------------------------------------------------------------------------------
#day 6 
#functions
#finding path in maze
#----------------------------------------------------------------------------------------------
#Day 7
#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = ["ardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
#-------------------------------------------------------------------------------------------------------------------------------------
#DAY 8
#----------------------------------------------------------------------------------------------------------------------------------------

#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#-----------------------------------------------------------------------------------------------------------------
#Day 9
#------------------------------------------------------------------------------------------------------------------

#find the tudent grade from the dictionary of the studenrt marks

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grade=student_scores.copy()
for i in student_grade:
 
  if student_grade[i]>91:
    student_grade[i]="Out sanding"
  elif student_grade[i]>=81 and student_grade[i]<=90:
    student_grade[i]="Exeeds expectations"
  elif student_grade[i]>=71 and student_grade[i]<=80:
    student_grade[i]="Exeeds expectations"  
  elif student_grade[i]<=70:
    student_grade[i]="Fail"  
print (student_grade)
#--------------------------------------------------------------------------------------------
   #DAY 10
#--------------------------------------------------------------------------------------------
#Calculator program

from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()





















































