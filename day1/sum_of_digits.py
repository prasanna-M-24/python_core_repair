def sum_of_digits(num):
    sum=0
    temp=num
    while (num!=0):
        digit=num%10
        sum=sum+digit
        num=num//10
    print("the sum of the digits of", temp,"is:",sum)
num=int(input("Enter a number:"))
sum_of_digits(num)
