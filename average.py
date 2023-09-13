a=int(input("tamil"))
b=int(input("english"))
c=int(input("maths"))
d=int(input("science"))
e=int(input("social"))
total=a+b+c+d+e
average=total/5
if(average<35):
    print("additional class is required")
else:
    print(" you are good to go")
