def factorial(num):
    fact=1
    if num==0:
        return 1
    else:
        for i in range (1,num+1):
            fact=fact*i
        return fact

num=int(input("Enter a number(positive):"))
print("The factorial of",num,"is:",factorial(num))
