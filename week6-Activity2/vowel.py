dict1 = {'a':1, 'b':2 , 'c':3}
dict2 = {'d':4, 'e':5 , 'f':6}

merged_dict = {**{k:v for k,v in dict1.items() if k in "aeioou"},
               **{k:v for k,v in dict2.items() if k in "aeioou"}}   

print(merged_dict)
