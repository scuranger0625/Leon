#[List]請創造記錄成績用的 list，並加入前五位學生的成績，分別為 88, 86, 94, 72, 83
#後來發現上述填入的成績 72 有誤，應改為 75
#請將學生成績排序後印出
#再加入五位學生成績，分別為 91, 60, 54, 72, 81
#請利用 list 相關的 method 或 function，計算成績的最高分、最低分、全距及平均

score = [88,86,94,72,83]

score2 =[91,60,54,72,81]

score.extend(score2)
#更改列表score中的72,也就是[3]或是[-2] 
score[-2] = 75

#將成績按照大小排序
#score.sort() 可將list中的數值由小到大 進行排列

score.sort()

print(score)

#將兩個列表直接相加 成為一個新的列表
#用extend改

#再將這個新的列表進行排列
score.sort()

print(score)

#定義最高分 最低分 全距(最大值-最小值) 平均
highest = max(score)
lowest = min(score)
fullrange = max(score) - min(score)

#sum(score)為計算列表中的數值總和
#len(score)用來計算列表score中元素的數量
#或是 average = sum(score)/10

average = sum(score)/len(score)

print("最高分為",highest)
print("最低分為",lowest)
print("全距為",fullrange)
print("平均為",average)


