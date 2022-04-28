def getInt(message):
  temp = 0
  while(True):
    try:
      temp = int(input(message))
      if temp < 0:
        print("Let's keep thing positive!")
      else:
        break
    except:
      print("That is not the proper value.")
  return temp

def getStr(message):
  while(True):
    temp = input(message)
    temp = temp.lower()
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      break
  return temp
  
def cipher(lower, other, encrypted, sentence, move):
  for letter in sentence:
    if letter in lower:
      pos = lower.find(letter)
      encrypted = encrypted + lower[(pos + move) % len(lower)]
      '''len(lower)'''
    elif letter in other:
      pos = other.find(letter)
      encrypted = encrypted + other[pos]
  print("The sentence you want to encrypt is:")
  print(encrypted)
  
def decipher(lower, other, encrypted, sentence, move):
  for letter in sentence:
    if letter in lower:
      pos = lower.find(letter)
      encrypted = encrypted + lower[(pos - move) % len(lower)]
      '''len(lower)'''
    elif letter in other:
      pos = other.find(letter)
      encrypted = encrypted + other[pos]
  print("The sentence you want to decrypt is:")
  print(encrypted)

def caesar(lower, other, encrypted):
  print("User manual: DECRYPTING: Automatically moves back. Do not enter a negative.")
  sentence = getStr("What sentence would you like to encrypt/decrypt? ")
  move = getInt("How many position would you like to shift it by? ")
  choice = getStr("Would you like to encrypt or decrypt? Write 'encrypt' or 'decrypt' ")
  if(choice == "encrypt"):
    cipher(lower, other, encrypted, sentence, move)
  elif(choice == "decrypt"):
    decipher(lower, other, encrypted, sentence, move)
  
caesar("abcdefghijklmnopqrstuvwxyz", " ,.?!@#$%^&*()-_+1234567890", "")