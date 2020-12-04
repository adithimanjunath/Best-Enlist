def merge(list1, list2): 

    merged_list = tuple(zip(list1, list2)) 
    return merged_list 

list1 = [1, 2, 3] 
list2 = ['a', 'b', 'c'] 
print(merge(list1, list2)) 


rng1 = list(range(1,8))
lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
print(lst1)

lst =lst(zip(lst1, rng1))
print(lst)

numbers = [6, 9, 3, 1]
print(numbers)
num = sorted(numbers)
print("sorted list : " ,num)

sequence_of_int = [ 1, 2, 4, 5, 7, 8, 9, 10, 13] 
filter_function = filter(lambda x: x % 2 != 0, sequence_of_int)
print(list(filter_function))
