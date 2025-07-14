import random

listOfWords = ["happy","sad","anxious","disapointed","fear","anger","love","depressed"]
string1 = random.choice(listOfWords)
lenOfstring = len(string1)
tries = 10
hiddenString = []
output = []


def checkChar(userChar):
  for characters in string1:
    if characters == userChar:
       return True

def hideString(string1):
  for i in range(0,len(string1)):
    hiddenString.append("_")
  

def Hangman():
  for i in range(0,len(string1)):
    userInput = input()
    if checkChar(userInput) == True and string1[i] == userInput:
      output.append(userInput)
      print("correct character correct position")
      print(output)

    elif checkChar(userInput) == True and string1[i] != userInput:
      print("correct character but wrong position")
      output.clear()
      Hangman()
      break

    elif checkChar(userInput) != True:
      print("thats the wrong letter")
      output.clear()
      Hangman()
      break

hideString(string1)
print(hiddenString)
Hangman()
