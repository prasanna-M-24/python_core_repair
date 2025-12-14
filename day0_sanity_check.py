def fun(num):
    for i in range (1,num+1):
        print(i)
    if num%2==0: 
            print("no. of odds:",num//2)
            print("no.of even:",num//2)
    else: 
            print("no od odds:",num//2+1)
            print("no.of even:",num-(num//2+1))

num=int(input("Enter any number:"))
fun(num)