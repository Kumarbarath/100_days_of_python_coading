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


