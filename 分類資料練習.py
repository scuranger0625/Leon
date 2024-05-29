import random

my_list = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "kiwi", "strawberry", "melon", "peach"]
replacement_values = [10, 20, 30, 40, 50]

# 將兩個列表合成一個新的列表
combined_list = my_list + replacement_values

# 隨機打亂順序
random.shuffle(combined_list)

print(combined_list)

#for迴圈
for i in combined_list :
    #isinstance檢查i是否為字串
    if isinstance(i,str) :
        print(i)

#for迴圈
for j in combined_list :
    #isinstance檢查j是否為數值
    if isinstance(j,int) :
        print(j)

        
        


