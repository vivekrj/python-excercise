count = 1
while count == 1:
 a,b,c = input("enter the three no:")
 d=a+b+c
 if d % 3 == 0:
   avg = d / 3
   print "avg is:",avg
 
 else:
   avg = d / 3.0
   print "avg is:", avg
 count = input("enter 1 to continue and  0 to quit:")