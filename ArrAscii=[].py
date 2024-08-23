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
    
    print(ArrAscii)
   