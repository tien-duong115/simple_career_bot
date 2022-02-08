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

from platform import architecture
import re
import long_responses as long
import json
import csv

path = open('/mnt/c/Users/tienl/class_proj/test.json')

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    
def get_data(path) -> json:
    data = json.load(path)
    return data

def available_category(data):
    unique_list = []
    for i in data['career']:
        if i['tags'] not in unique_list:
            unique_list.append(i['tags'])
    return unique_list


def check_all_messages(message, source_data):
    highest_prob_list = {}
    # Simplifies response creation / adds it to the dict
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        
    ### Open data file and store available majors into list        
    available_major = available_category(source_data)

    # Responses -------------------------------------------------------------------------------------------------------
    
    ### Casual Response by original source
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    
    

    ### Category responses base on available value within dataset 
    ### Create 1 response for every available Major
    for major in available_major:
      response(f'{major}' , [major], required_words=[major])  
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    ### If response found match with Dataset's Major category tags, we recommend the Majors
    for ele in data['career']:
        if ele['tags'] == best_match:
            print(f"\nResult are base from search: \n >>> [{ele['major']}]")

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

    

# Used to get the response
def get_response(user_input):
    global usr_input
    usr_input = user_input
    
    if user_input == quit:
        return quit
    
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message,data)
    return response


# Testing the response system
print("\n        WECLOME TO CAREER CHATBOT version 0.0.2 \U0001F923 \n")

#######################################################  DRAWING THE HEART #################################################################
n = 10
# upper part of heart
for i in range(n//2, n, 2):
    # print first spaces
    for j in range(1, n-i ,2):
        print(" ", end="")
    # print first stars
    for j in range(1, i+1, 1):
        print("*", end="")
    # print second spaces
    for j in range(1, n-i+1, 1):
        print(" ", end="")
    # print second stars
    for j in range(1, i+1, 1):
        print("*", end="")
    print()

# lower part
for i in range(n,0,-1):
    for j in range(i, n, 1):
        print(" ", end="")
    for j in range(1, i*2, 1):
        print("*", end="")
    print()
#######################################################  END OF THE HEART #################################################################

data = get_data(path)
available_major = available_category(data)

print("  PLEASE TYPE YOUR FIELD OF INTEREST\n")
print("  HERE SOME OF THE AVAILABLE MAJOR MIGHT OF YOUR INTEREST\n")

# Print out pair value of available major
mlist = list(zip(available_major[::2], available_major[1::2]))
for e,i in enumerate(mlist):
    print(f"        {e+1}.{i}")
    
    
# Starting Bot engine
while True:
    print("\n              To EXIT type quit  \n")
    print('\nbot: ' , get_response(input('\U0001f600 \nYou: ')))
    if usr_input == "quit":
        break

    
