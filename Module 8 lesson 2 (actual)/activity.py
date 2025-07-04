my_tuple = ("Tisha", "Lena", "Sora", "Gio")

#accessing an element
print(my_tuple[1])

#slicing
print(my_tuple[0:3])

#nested tuple
new_tuple = ("mouse", ("Tisha", "Lena", "Sora", "Gio"))
print(new_tuple)

#iteration
for letter in new_tuple:
    print("Hello", letter)