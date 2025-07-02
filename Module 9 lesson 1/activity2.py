my_dict = {'name': 'Tisha','age': '14','nationality': 'Indian','learner': 'Student'}

print(my_dict['name'])        
print(my_dict.get('age'))    

# Update any value
my_dict['learner'] = 'teacher'
print(my_dict)                

# Add a new item
my_dict['district'] = 'Indonesia'
print(my_dict)               

# Pop (remove) an item
my_dict.pop('age')
print(my_dict)         

# Clear all items
my_dict.clear()
print(my_dict)