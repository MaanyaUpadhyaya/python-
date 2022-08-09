"""class of books"""

class Book:
  title=","
pages=0
def __init__(self,t,p):
  self.title=t
  self.pages=p

def __add__(self,other):
  return(Book(self.title,self.pages+other.pages))
a=Book("A",30)
b=Book("A",40)

c=a+b
print(c.pages)

"""complex numbers"""

class complex:
 def read(self):
  print("a+ib and x+iy")
  self.a=int(input(" Enter a=:"))
  self.b=int(input(" Enter b=:"))
  self.x=int(input(" Enter x=:"))
  self.y=int(input(" Enter y=:"))
  self.ch=input(" Enter - or * : ")

def comp(self):
 if(self.ch=="-"):
  print(" a+ib - x+iy = %d + i %d"%(self.a-self.x,self.b-self.y))
 elif(self.ch=='*'):
  print(" a+ib * x+iy = %d + i %d"%(self.a*self.x-self.b*self.y,self.a*self.y+self.b*self.x))
 else:
  print("INVALID")

ob=complex()
ob.read()
ob.comp()