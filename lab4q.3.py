num=input("enter the number:")
total=0
for i in range(len(num)):
  digit=int(num[i]) # note the important step here typecasting plus indexing to get individual digit.
  total= total+digit
print("the sum of the digit of the number is:\n",total)
