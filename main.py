import random

listOfWords = ["happy","sad","anxious","disapointed","fear","anger","love","depressed","sorrow","dread","excitement","joy","calm","enjoyment","shame"]
string1 = random.choice(listOfWords)
lenOfstring = len(string1)
hearts = 5
hiddenString = []


def checkChar(userChar):
  for characters in string1:
    if characters == userChar:
       return True

def hideString(string1):
  for i in range(0,len(string1)):
    hiddenString.append("_")
  

def Hangman(hearts):
  x = hearts
  if x > 0:
    for i in range(0,len(string1)):
      userInput = input(">> ")
      if checkChar(userInput) == True and string1[i] == userInput:
        hiddenString[i] = userInput
        print("correct character correct position""\n")
        print(hiddenString)

      elif checkChar(userInput) == True and string1[i] != userInput:
        print("correct character but wrong position, word has been reset""\n")
        hiddenString.clear()
        hideString(string1)
        Hangman(x)
        break

      elif checkChar(userInput) != True:
        print("thats the wrong letter, word has been reset and you lose a heart")
        hiddenString.clear()
        hideString(string1) 
        x -= 1
        print(f"Heres your remaining hearts {x} 🎔""\n")
        Hangman(x)
        break
  else:
    print("YOU LOSE!!!")

def winOrlose():
  for x in string1:
      for y in hiddenString:
        if x == y:
          return True
        
def didYouWin():
  if winOrlose() == True:
    print("YOU WIN!!!!")

  
# Function calls before game
hideString(string1)

#################################################################
#Make shift UI:
print("\n\n""#############################################""\n"  
            "# Game of Hangman                           #""\n"
            "# guess words based on the theme 'feelings' #""\n"
            "#############################################"
      "\n\n")
print(f"Num of hearts: {hearts} 🎔""\n")
print(hiddenString)
#################################################################

# The game
Hangman(hearts)
didYouWin()
##################################################################