'''Re-arange names. Make it so that it right my name, then loops to the beginning and adds one. when it's done looping make a second loop to have it restart at zero'''
def getStr(message):
  while(True):
    temp = input(message)
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      break
  return temp
  
def box(loop, anem):
  # starts at 0
  length = len(name)
  for i in range(loop, length, 1):
    print(name[i], end = ' ')
  
  
  if loop > 0:
    for j in range(0, loop, 1):
      print(name[j], end = ' ')
  loop += 1
  if loop == length:
    print("")
    print("This name is now a abomination. Your welcome!")
  else:
    print("")
    box(loop, name)

name = getStr("What name would you like to become a abomination? ")
box(0, name)

#Don't steal :(
  