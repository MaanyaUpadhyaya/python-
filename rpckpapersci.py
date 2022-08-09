print(" 1. Rock\n 2. Scissor\n 3. Paper \n chose\n")

while True:
  a=int(input(" Player 1: "))
  b=int(input(" Player 2: "))
  if(a==1 and b==2):
   print(" congrats Player 1 ")
  elif(a==2 and b==1):
    print(" congrats Player 2 ")
  if(a==2 and b==3):
   print(" congrats Player 1 ")
  elif(a==3 and b==2):
   print(" congrats Player 2 ")
  if(a==3 and b==1):
   print(" congrats Player 1 ")
  elif(a==1 and b==3):
   print(" congrats Player 2 ")
  if(a==b):
   print("Tie")
  if(input(" press yes to start a new game ")=="yes"):
     continue
  else:
     break