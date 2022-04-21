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
  temp = input(message)
  while(True):
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      break
  return temp
  
def splicer(word, i, s):
  print(word[i:s + 1])

def main():
  while(True):
    word = getStr("What world do you want in the splicer? ")
    length = len(word)
    i = getInt("What index value of the word do you want the splicer to start at? ")
    print("Dev note: I made it so that is will add 1 to the s value. So make it the last number you want and it will fix the rest for you.")
    s = getInt("What index value of the word do you want the splicer to end at? ")
    '''////////////////////////////////////////////////////////////////'''
    if s > length and i <= 0:
      print("Sorry pal, "+ str(s) + " is greater then " + str(length) +"or, " + str(i) + " is lesser then 0.")
    elif s < length and i >=0:
      splicer(word, i, s)
      break
      
main()