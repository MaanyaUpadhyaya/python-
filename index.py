"""prime numbers """
for i in range(2,int(input("Enter end range"))+1):
  for x in range(2,i):
    if(i%x==0):
      break
    else:
      print(i,end=",")


"""numbers divisible by 7"""
for i in range(2000,3201,5):
  if(i%7==0):
    print(i, end=",")



""""character cound and word count"""
n=input("Enter string ")
l=0
a=n.split()
print(" No. of words is ",len(a))
for i in a:
  l+=1
  print("Length of %s is %d"%(i,len(i)))



""""searching .py files in a directory"""
import os
for i in os.listdir():
  if(i.endswith(".py")):
   print(i)


""""number of lines ina file"""
f= open("test.txt",'r')
i=0
while(f.readline()!=""):
  i+=1
  print(" No. of lines in file is ",i)
f.close()


"""copying file content"""
import os
f1=open(";test.txt",'r')
r=f1.read()
f1.close()
if(os.path.exists("disti.txt")):
  print(";File already exists ")
else:
  f2=open(";disti.txt",'w')
f2.write(r)
f2.close()
print("Content of disti.txt")
for i in open("disti.txt").read().split("\n"):
  print(i)


"""dict ti return i*i"""
d={}
for i in range(1,int(input("Enter n "))+1):
  d.update({i:i*i})
print(d)


"""2nd largest and 2nd smallest number"""
l=[]
for i in range(0,int(input("Enter limit "))):
  l.append(int(input("Enter ")))
l.sort()
print("Second largest is %d second smallest is %d"%(l[-2],l[1]))


"""recursive function of a factorial"""
def fact(n):
  if(n==0): 
   return 1
  if(n==1):
    return 1
    return(n*fact(n-1))
n=int(input("Enter n "))
print("Factorial is ",fact(n))


""""""


