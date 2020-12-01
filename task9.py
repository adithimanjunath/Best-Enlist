r = lambda x, y: x * y
print(r(12, 3)) 

def fibonacci(count): 
    fib_list = [0, 1] 

    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), 
        range(2, count))) 

    return fib_list[:count] 

print(fibonacci(10)) 


num = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", num)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,num))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

my_list = [12, 18, 54, 36, 102, 54, 669,]
result = list(filter(lambda x: (x % 9 == 0), my_list))
print("Numbers divisible by 9 are",result)

array_num = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_num)
even = len(list(filter(lambda x: (x%2 == 0) , array_num)))
print("\nNumber of even numbers in the above array: ", even)

