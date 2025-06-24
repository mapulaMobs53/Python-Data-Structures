#unordered elements, they do not allow duplicates and can add or delete
'''
my_set = {1,2,3,4,5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
'''

#union basically concates and removes duplicates

set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)

#intersection finds the common element
interset = set1.intersection(set2)
print(interset)

#difference finds the difference 
diff = set1.difference(set2)
print(diff)