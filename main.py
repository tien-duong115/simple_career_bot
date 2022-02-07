from platform import architecture
import re
import long_responses as long
import json
import csv


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
    

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    def available_category(data):
        unique_list = []
        for i in data['career']:
            if i['tags'] not in unique_list:
                unique_list.append(i['tags'])
        return unique_list
        
    ### Open data file and store available majors into list        
    f = open('/mnt/c/Users/tienl/class_proj/test.json')
    data = json.load(f)
    available_major = available_category(data)

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
            print(f"Result are base on your interest\n\nYou can look into: [{ele['major']}]")

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

    

# Used to get the response
def get_response(user_input):
    
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
print("\n        WECLOME TO CAREER CHATBOT version 0.0.1 \U0001F923 \n")
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
print("     PLEASE TYPE YOUR FIELD OF INTEREST, EXAMPLE: arts\n")

while True:
    print("              To EXIT type quit  \n")
    print('bot: ' + get_response(input('\U0001f600 You: ')))
