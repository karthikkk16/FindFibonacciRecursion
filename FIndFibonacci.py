def FindFibonacci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return FindFibonacci(number-1)+FindFibonacci(number-2)
number=int(input())
print(FindFibonacci(number))