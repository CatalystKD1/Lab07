def getInt(message):
  temp = 0
  while(True):
    try:
      temp = int(input(message))
      break
    except:
      print("That is not the proper value.")
  return temp
  
def getStr(message):
  while(True):
    temp = input(message)
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      break
  return temp

def looper(word, i, s, length):
  for j in range(i, s, 1):
    print(word[j], end = '')

def main():
  while(True):
    word = getStr("What world do you want in the looper? ")
    length = len(word)
    i = getInt("What index value of the word do you want the looper to start at? ")
    s = getInt("What index value of the word do you want the splicer to end at? ")
    if s > length and i <= 0:
      print("Sorry pal, "+ str(s) + " is greater then " + str(length) +"or, " + str(i) + " is lesser then 0.")
    elif s <= length and i >=0:
      looper(word, i, s, length)
      break

main()