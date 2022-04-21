# if you are looking for the hard one, it's in part04
def getStr(message):
  while(True):
    temp = input(message)
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      break
  return temp

def reverser(word):
  length = len(word)
  for i in range(length - 1, -1, -1):
    print(word[i], end = ' ')
def main():
  word = getStr("What world would you like to reverse? ")
  reverser(word)
  
main()