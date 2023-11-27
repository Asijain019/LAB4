N= int(input("Enter the positive integer:"))
i=1
fact=1
if N==0:
    print("the factorial of the given number",N,"is 1")
elif N<0:
    print("invalid input")
else:    
    while i<=N:
        fact*=i
        i+=1
    print(f"the factorial of the given number {N} is equal to:\n",{fact})


