num = ['10', '20', '30']
print('num list:' , num)
num.append('40')
print('Updated num list: ', num)
num.remove('10')
print('updated num list:' , num)
a = max(num)
b = min(num)
print(a)
print(b)

tuple1 = (2,4,6,8,10)
new1 =tuple(reversed(tuple1)) 
print(new1)

tuple2 = (3,6,9,12,15)
new2 = list(tuple2)
print(new2)

