import json
import csv
import re
import pandas as pd
# with open ('majors-list.csv', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     next(reader)
#     Agriculture = [i for i in reader if re.search("^Agriculture", i[2])]


# def split_repose(mlist):
#     output = []
#     for i in mlist:
#         for e in i:
#             output.append(e)
#     return output

# print(split_repose(Agriculture))




# def read_file(path):
#     with open(path) as file:
#         df = pd.read_csv(file)
#         df = df[['Major', 'Major_Category']]        
#     return df

# def to_dict(df):
#     return dict(zip(df.Major.str.lower(), df.Major_Category.str.lower()))
    
# path = 'majors-list.csv'

# df = read_file(path)

# dict_data = dict(zip(df.Major.str.lower(), df.Major_Category.str.lower()))

# print(dict_data)

# f = open('/mnt/c/Users/tienl/class_proj/test.json')
# data = json.load(f)

    
# def available_category(data):
#     unique_list = []
#     for i in data['career']:
#         if i['tags'] not in unique_list:
#             unique_list.append(i['tags'])
#     return unique_list
    
# available_major = available_category(data)

# for ele in available_major:
#     print(ele)


# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
#             result_str=result_str+"M "    
#         else:      
#             result_str=result_str+"  "    
#     result_str=result_str+"\n"    
# print(result_str);

# # heart pattern 
# n = 10

# # upper part of heart
# for i in range(n//2, n, 2):
#     # print first spaces
#     for j in range(1, n-i ,2):
#         print(" ", end="")
#     # print first stars
#     for j in range(1, i+1, 1):
#         print("*", end="")
#     # print second spaces
#     for j in range(1, n-i+1, 1):
#         print(" ", end="")
#     # print second stars
#     for j in range(1, i+1, 1):
#         print("*", end="")
#     print()

# # lower part
# for i in range(n,0,-1):
#     for j in range(i, n, 1):
#         print(" ", end="")
#     for j in range(1, i*2, 1):
#         print("*", end="")
#     print()

def foo():
    global z
    z = 10
foo()
print(z)