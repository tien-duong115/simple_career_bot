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
        

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    # response('See you!', ['bye', 'goodbye'], single_response=True)
    # response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    # response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    # response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    
    def split_repose(mlist):
        for i in mlist:
            for e in i:
                print(e)
        # return output
    
    with open ('majors-list.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        Agriculture = [i for i in reader if re.search("^Agriculture", i[2])]
    

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    
    response('agriculture' , ['agriculture'] , required_words=['agriculture'])

    temp = {'agriculture': ['something', 'something']}
    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    result = []
    for k, v in temp.items():
        if best_match == k:
            print(f'\n{Agriculture}\n')
            # result.append(v)
    
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match



# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('bot: ' + get_response(input('You: ')))
