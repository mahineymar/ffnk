n=int(input())
a=0
for x in range(1,n+1):
  if(n%x==0):
   a=a+1
if(a==2):
  print("yes")
else:
  print("no")
