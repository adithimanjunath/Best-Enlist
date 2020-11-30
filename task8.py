print("Choose the operation")
print("1 Addition \t 2 Subraction \t 3 Multiplication \t 4 Division")
c = int(input("Enter the choice "))
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

try:
    if (c == 1):
        d = a + b
except:
    print("Not valid")

try:
    if (c == 2):
        e = b - a
except:
    print("not valid")
    
try:
    if (c == 3):
        f = a * b
except:
    print("not valid")

try:
    if (c == 4):
        g = a / b
except:
    print("not valid")


try:
    raise NameError('Adithi')
except NameError:
    print("Handeled")
    
while True:
    try:
         a = int(input("Enter a digit : ")
         print("The didgit youve enterd is : " , a)
         break
    except:
        print("inavlid digit")
print("Success")
    
