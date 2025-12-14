def fun(num):
    odd_count=0
    even_count=0
    for i in range (1,num+1):
        if i%2==0: 
            even_count+=1
            print(i,"-> Even")
        else:
            odd_count+=1
            print(i,"-> Odd")
    print("total odds:",odd_count)
    print("total even:",even_count)
            
num=int(input("Enter any number:"))
fun(num)