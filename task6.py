n = [2,4,6,8,10]
for i in n:
    print("After addition: ", i+2)
    
    
 n=5
for i in range(0 , n+5):
    for j in range(n-i , 0 , -1):
            print(j , end=' ')
    print()
 
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
print(sum)

num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")
   
 n = 9
for i in range(1, 11):
   print(n, 'x', i, '=', n*i)
   
 n = float(input("Enter a number: "))
if n >= 0:
   if n == 0:
       print("Neutral")
   else:
       print("Positive number")
else:
   print("Negative number")
  
print("Enter days: ")
d = int(input())
y = (d / 365)
w = (d % 365) / 7
print("years : " , y)
print("days :" , w)

import math 
  
a = math.pi/6

print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a)) 

print("CALCULATOR")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("INVALID")
