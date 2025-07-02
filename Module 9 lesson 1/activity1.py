my_list=['pencil', 'eraser', 'sharpner', 'notebook', 'pencil bag']

#length
print("The length of this list is", len(my_list))

#Accessing the element of the list
print("First element:", my_list[0])
print("Third element:", my_list[2])

#append
my_list.append('coloring pencils')
print("Updated list after adding:", my_list)

#remove
my_list.remove('notebook')
print("Updated list after removing:", my_list)

#sorting
my_list.sort()
print("Sorted List:", my_list)

#pop
my_list.pop(2)
print("List after popping an item out:", my_list)

#reverse list
my_list.reverse()
print("Reversed list:", my_list)

#slicing
my_list = my_list[0:3]
print("List after slicing:", my_list)