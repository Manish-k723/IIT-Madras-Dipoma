def odd_one(lst):
    data_types = {}
    for element in lst:
        data_type = str(type(element).__name__)
        if data_type in data_types:
            data_types[data_type]+=1
        else:
            data_types[data_type] =1
            
    for i,j in data_types.items():
        if j==1:
            return i
    
print(odd_one(eval(input().strip())))