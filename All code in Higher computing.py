temperatures = [11.21, 2.68, 3.91, 4.11]
total = 0

# Loop through the numbers and add them to the total
for counter in range(0, 4):
   # Get the ‘current’ temperature and convert to integer
   temp = temperatures[counter]
   temp = int(temp)
   
   # Add shortened temp to the total
   total = total + temp

print(total)

#---------------------------------------------------------------------------------------------
#Task 1
# Ask the user to enter a number
num = int(input("Please enter a number"))


# Divide by 2 to get the remainder
remainder = num % 2
# If remainder is 0, number is even
if remainder == 0:
   print("This is an even number")
else:
   print("This is an odd number")
   
      
#---------------------------------------------------------------------------------------------
# Multiples of five??
#Task 2
import random
# An array of numbers
nums = [] * 10


# Loop 10 times
for i in range(1, 12):
  print(nums)
  ranNum = random.randint(0, 500)
 
 #add the numbers to a variable
  nums.append(ranNum) 
 
  remainder= ranNum % 5


  #check if the number is divisible of 5 or print otherwise

  if remainder == 0:
    print("Your number is a multiple of 5! ")
  else: 
    print ("Your number is not a multiple of 5! ")

#---------------------------------------------------------------------------------------------

# Start the clock
clock = 1

# Infinite loop (while true, so loop will run forever)
while True:
   clock = clock + 1
   remainder = clock % 12
   # If there is a remainder, subtract 12
   if remainder == 1:
      clock = clock - 12# Multiples of five??


#-----------------------------------------------------------------------------------------------
#task 3
# Get twelve temperatures
temps = [] * 12
total=0

for counter in range (0,12):
    counter= counter+1
    temp= float(input("Please enter the " + str(counter) + " temperature: "))
    temps.append(temp)

for n in range(0,12):
    convert= int(temps[n])
    total = total + convert

remainder = total % 2
if remainder == 0:
    print("Your total temperature " + str(total) + " is an even number. ")
else: 
    print("Your total temperature " + str(total)+ " is an odd number. ")


#-------------------------------------------------------------------------------------------

char=input("Please enter a character: ")


lenChar=len(char)
while lenChar != 1:
    char =input("Invalid input! please enter your character again!: ")


char_code=ord(char)


lenChar=len(char)
if lenChar != 1:
    char =input("Invalid input! please enter your character again!: ")


if char_code >=65 and char_code <=90:
    print("Your character is an upper case letter")


elif char_code >=97 and char_code <=122:
    print("Your character is a lower case letter")


else:
    print("Your character is not a letter!")
#--------------------------------------------------------------------------------------------------------
# Get initials from first name and surname, using two separate substrings

firstName = input("Enter first name: ")
secondName = input("Enter second name: ")

middleAnswer = input("Do you have a middle name (Yes or No)?: ")

first_initial = firstName[0:1]
second_inital=secondName[0:1]



if middleAnswer == "Yes" or middleAnswer == "yes":
    middleName = input("Please enter your middle name: ")
    middle_initial=middleName[0:1]
    print(firstName + " " + middleName + " " + secondName + "," + " Your initials of your names are: " + first_initial + middle_initial + second_inital)

else: 
    print(firstName + " " + secondName + " Your initials of your names are: " + first_initial + second_inital)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

