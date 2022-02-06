from functions import *

# create chatbot 
home_bot = create_bot('Jordan')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ").lower()
owner = "mark"
if identity == owner:
    print("Welcome, Mark. Happy to have you at home.")
elif identity == "jane":
    print("Mark is out right now, but you are welcome to the house.")
else:
    print("Your access is denied here.")
# rules for responding to different identities
# write your code here

# custom data
house_owner = [
    "who is owner of this house?",
    "wark Nicholas is the owner of this house."
]
custom_train(home_bot, house_owner)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
# write your code heremark
if identity == owner:
    birth_loc = ["where was i born?", "You were born in Alaska"]
    favorite_book = ["what is my favorite movie?", "you have watched dinosaur good more then 200 times."]
    favorite_sport = ["what is my favorite sport", "you have always loved chess"]
custom_train(home_bot, birth_loc)
custom_train(home_bot, favorite_book)
custom_train(home_bot, favorite_sport)
# start chatbot
start_chatbot(home_bot)