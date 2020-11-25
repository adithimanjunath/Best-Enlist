//Merge 2 dictionaries
dict1 = {'adithi': 80, 'Tanu': 90}
dict2 = {'Disha': 100, 'Namrata': 110}
dict = dict1.copy()
dict.update(dict2)
print(dict)

//remove a key from dictionary
dict = {'a':2,'b':4,'c':6,'d':8}
print(dict)
if 'a' in dict: 
    del dict['a']
print(dict)

//map 2 lists into a dictionary
list1 = ['Adithi', 'Tanu', 'Disha']
list2 = ['Mysore','Bangalore', 'Mumbai']
dictionary = dict(zip(list1, list2))
print(dictionary)

//length of a set 
sets = set([5, 10, 15, 20, 25 , 30 , 35])
print(len(sets))

//remove the intersection of a 2nd set from the 1st set
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("Original sets are:")
print(set1)
print(set2)
print("Remove the intersection of a 2nd set from the 1st set")
set1.difference_update(set2)
print(set2)
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set")
print(set1-set2)



