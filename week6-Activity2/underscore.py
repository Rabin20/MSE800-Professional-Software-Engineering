# x,_,y = (1,"ignore", 3)
# print (x, y)

# names = ['Alice', 'Bob', 'Charlie']

# for i in range(len(names)):
#     print(i, names[i])

# for i, name in enumerate(names):
#     print(i, name)

# for i, name in enumerate(names, start=1):
#     print(i, name)

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]

# # # Create a dictionary using the zip function
# my_dict_zip = dict(zip(names, ages))
# print(my_dict_zip)

# paired = list(zip(names, ages))
# print(paired)

# ##print datatypes
# print(type(my_dict_zip))
# print(type(paired))

ids = [1, 2, 3]
names = ['Alice', 'Bob', 'Charlie', 'David']
grades = ['A', 'B', 'A+', 'A']

students = list(zip(ids, names, grades))
print(students)

students_dict = {id: {names, grades}for id, names, grades in students}
print(students_dict)