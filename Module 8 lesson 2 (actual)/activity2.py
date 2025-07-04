my_set = {1,1,1,2,2,2,2,3,3,4,4,4,5,5,5}
print(my_set)

#add
my_set.add(6)
print(my_set)

set1 = my_set
set2 = {2,4,6,8,10}

set_intersection = set1.intersection(set2)
print(set_intersection)

#set union
set_union = set1.union(set2)
print(set_union)

#set difference
set_difference = set1.difference(set2)
print(set_difference)

#set symmetric difference
set_symmetric_difference = set1.symmetric_difference(set2)
print(set_symmetric_difference)