keys = ['a' , 'b','c']
values = [1, 2, 3]
# Create a dictionary using a dictionary comprehension
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)
# Create a dictionary using the zip function
my_dict_zip = dict(zip(keys, values))
print(my_dict_zip)