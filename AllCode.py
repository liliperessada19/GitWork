# All previous code 
#1. How to find out the remainder of two random numbers and store it in a variable

import random
num = random.randint(1,100)
 #the percentage symbol is used to divide the random number by two and stores the remainder left over after dividing in the variable "remainder"
remainder =  num % 2
 
print(num)

#----------------------------------------------------------
#2. Cutting off the digits after a decimal point of a float by converting into aninteger
pupilMarks = [] * 10

for counter in range (0, 10):
    TeacherInput = float(input("enter the number:  "))
    convert = int(TeacherInput)
    pupilMarks.append(convert)

print(pupilMarks)

#----------------------------------------------------------
#3. Finding out the ASCII value of a character and storing it in a variable to be able to check whether it's a capital letter or not
char=input("Please enter a character: ")

#Ord is the command that actually turns the character into it's assigned ASCII value in the computer
char_code=ord(char)

# To check if the character is a capital letter then check if that character value is within all the capital letter values and print a success message
if char_code >=65 and char_code <=90:
    print("Your character is an upper case letter")
else:
    print("Your character is not a capital letter!")

#----------------------------------------------------------
#4. How to get the first character of an expression and store that in a variable to create a username that aks for their last name, and full name but only takes their first inital

#Ask for the users first and last name
firstName=input("Please enter your first name: ")
lastName=input("Please enter your last name: ")

#Then to get the first letter of their name use the square brackets and enter the number of the position of the string you would like
firstInit=firstName[0:1]

#then combine that into a username
print("Your username is : " + lastName + firstInit)

#----------------------------------------------------------
#5. Print out the ASCII values of a message of the users choice

#Declare all empty arrays and ask for user input
ArrAscii=[]
ArrLetters=[]
ArrAll=[]
message=input("Please enter any message: ")


for counter in range (0, len(message)):
#Create a variable that stores the first character of the message and adds one to the loop until it cycles through the whole message seperately
    char=message[counter:counter+1]
#create another variable that stores the ASCII value of whatever character the loop is on and append that to an array
    num=ord(char)
    ArrAscii.append(num)
    
#print the ASCII values of all the characters in the message
    print(ArrAscii)

#----------------------------------------------------------
#6. Grammar check a sentence by checking if the first letter is a capital letter and the last is appropriate punctuation
sentence=input("Please enter a sentence: ")

#Take the last character of the sentence and convert it to ASCII
lastChar= sentence[-1]
print(lastChar)
gramCheck=ord(lastChar)

#Take first character of the sentence and convert it to ASCII
capChar=sentence[0:1]
capCheck=ord(capChar)

#----------------------------------------------------------
#7. Check if a word / phrase is the same backwards as it is forwards

#Get an input from the user and initalize variables
sentence=input("Please enter a word or phrase: ")
len=len(sentence)

reversed=[]*len
checkArr=[]*len
count=-1

for counter in range (0,len):
#get the last character of the sentence and loop through from the last character to the first until every character is done
    char=sentence[len-1:len]
#take one away from the length so that the program knows to move onto the 2nd last letter of the sentence and so on
    len=len-1
    reversed.append(char)

#Check if the sentence reversed is the same as the original sentence and store in a variable called check
check=reversed[count+1] == sentence[count+1]
checkArr.append(check)
