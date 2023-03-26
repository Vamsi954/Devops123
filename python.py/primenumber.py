num = int(input("Enter the number: "))
if num == 1:
    print('It is not a prime number')
elif num>1:
    for i in range(2, num):
        if num%i == 0:
            print("is not a prime number")
    else:
        print("is a prime number")
#if input number is <or= 1 then
else:
    print("it is not a prime number")
    