
uni_char = {}
current_max = 0
window_start = 0
k = 3
mstring ='araaaaaaaaaaaaaa'
for window_end in range(len(mstring)):
    right = mstring[window_end]
    if right not in uni_char:
        uni_char[right] = 0
    uni_char[right] +=1
    
    while len(uni_char) > k:
        left = mstring[window_start]
        uni_char[left] -=1
        if uni_char[left] == 0:
            del uni_char[left]
        window_start+=1
    current_max = max(current_max, window_end - window_start +1)

print(current_max)
     