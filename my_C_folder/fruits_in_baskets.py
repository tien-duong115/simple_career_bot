mstring = ['A', 'B', 'C', 'A', 'C']

fruit_basket = {}
window_start = 0
current_max = 0

for window_end in range(len(mstring)):
    right_fruit = mstring[window_end]
    
    if right_fruit not in fruit_basket:
        fruit_basket[right_fruit] = 0
    fruit_basket[right_fruit] +=1
    
    while len(fruit_basket) > 2:
        left_fruit = mstring[window_end]
        fruit_basket[left_fruit] -= 1
        if fruit_basket[left_fruit] == 0:
            del fruit_basket[left_fruit]
        window_start +=1
    current_max =max(current_max, window_end - window_start +1)

print(current_max)