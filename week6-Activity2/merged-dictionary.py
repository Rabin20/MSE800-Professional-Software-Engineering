dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}
# Merge dictionaries using dictionary comprehension
merged_dict = {**dict1, **dict2, **dict3}
merged2 = {**dict2, **dict3, **dict1}
merged3 = {**dict3, **dict1, **dict2}
print(merged_dict)
print(merged2)
print(merged3)