x= int(input("enter the value foe x:"))
y=int(input("enter the value for y:"))
N=int(input("enter the value for the third integer:"))
for i in range(x,y+1):
    if i%N==0:
        print(i)
        
