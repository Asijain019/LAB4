N = int(input("Enter the number which you wish to check:"))

if N < 2:
    print("Invalid input")
else:
    for i in range(2, N):
        if N % i == 0:
            print("Not a prime number.")
            break
    else:
        print("It is a prime number.")
