dic1 = {'A': 100, 'B': 200}
dic2 = {'D': 300, 'C': 200}
dic = dic1.copy()
dic.update(dic2)
print(dic)

dict={'a':20,'b':40,'c':60,'d':80}
del dict['d']
print(dict)

keys=['color:1','color:2','color:3','color:4']
colors=['red','blue','green','pink']
res = {}
for key in keys:
   for value in colors:
      res[key] = value
      colors.remove(value)
      break
print("Dictionary from lists :\n ",res)

seta=set([12,1,0,13,14,15,1,61,70,500,1000])
print(len(seta))

s1={2,4,6,8,10,12}
s2={3,6,9,12,15,18}
print("original sets:");
print(s1);
print(s2);
print("remove the intersection of a 2nd set from the 1st set using difference_update():");
se1.difference_update(s2)
print(s1);
set1={1,4,9,16,25,36}
set2={3,6,9,12,15,18}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:");
print(set1-set2);
