import random
import string

def getInt(message):
  temp = 0
  while(True):
    try:
      temp = int(input(message))
      if(temp >= 3):
        break
    except:
      print("That is not the proper value.")
  return temp

def alphabet():
  temp = string.ascii_letters
  return( ''.join(random.choice(temp) for i in range(1)) )

def digits():
  letters = string.digits
  return ( ''.join(random.choice(letters) for i in range(1)) )
  
def punctuation():
  letters = string.punctuation
  return( ''.join(random.choice(letters) for i in range(1)) )
         
def generator():
  password = ""
  length = getInt("How long would you like your pasword to be? Must be longer then 3: ")
  for i in range (length):
    if(length == 3):
      password = password + digits()
      password = password + punctuation()
      password = password + alphabet()
      break
    else:
      h = random.randint(0, 2)
      if(h == 0):
        password = password + digits()
      elif(h == 1):
        password = password + punctuation()
      elif(h == 2):
        password = password + alphabet()

  print(f"Your password is  {password}  !")
  print("Have a good day!")

generator()