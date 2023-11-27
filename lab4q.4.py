N=int(input("enter the value N:"))
divisible_count=0
not_divisible_count=0
while True:
    num=int(input("Enter the number till -999 is entered:"))
    if num==-999:
        break
    if num%N==0:
        divisible_count +=1
    else:
        not_divisible_count +=1
print("count of the numbers divisible by ",N,":",divisible_count)
print("count of the numbers not divisible by ",N,":",not_divisible_count)

            
