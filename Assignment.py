#Python program to check whether the given number is even or not.
num=int(input("Enter the number: "))
if num%2==0:
    print("The number" , num , "is even" )
else:
    print("The number" , num , "is odd")
    

#Python program to convert the temperature in degree centigrade to Fahrenheit
temp=float(input("Enter the temperature: "))
form=((temp*(9/5))+32)
print("The Fahrenheit value is",form)


#Python program to find the product of a set of real numbers
num1=list(map(float,input().split()))
c=1
for i in num1:
    prod=c*i
    c=prod
print("The product value is :",prod)


#Python program to find the factorial of a number using recursion
def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)
num=int(input("Enter the number: "))
if num<0:
    print("There is no value for negative number")
elif num==0:
    print("The value is 1")
else:
    print("The value is",factorial(num))
    
    
#Python program to implement linear search
num=int(input())
arr=list(map(int,input().split()))
l=[]
for x in arr:
    if x==num:
        l.append(x)
if len(l)>0:
    print('The number is found by linear search')
else:
    print('The number is not present in the list')
    
#Python program to implement binary search
def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        mid = (high + low) // 2  
        if list1[mid] < n:  
            low = mid + 1  
        elif list1[mid] > n:  
            high = mid - 1  
  
        else:  
            return mid  
    return -1   
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 45  
result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")  




#Python program to find the largest number in a list without using built-in functions
l=list(map(int,input().split()))
c=0
a=0
for i in l:
    if l[a]>c:
        c=l[a]
    else:
        c=c
    a+=1
print(c)



#Python program to delete an element from a list by index
n=int(input())
l=list(map(int,input().split()))
l.pop(n)
print(l)


#Python program to print all the items in a dictionary
dic={'Surya':24,
     'Bhavana':24,
     'Bharathi':22,
     'Sarathi':18 }
for key , value in dic.items():
    print(key,':',value)
    

#Python program to find the average of 10 numbers using while loop
avg=[int(i) for i in input("Enter the 10 numbers: ").split()][:10]
c=0
a=0
while c<10:
    a=avg[c]+a
    c+=1
aver=a/10
print("The average of 10 number is :",aver)
    
    












































    
    

        
        
        
    


























