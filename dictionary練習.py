#[dictionary]
# 請用利 dictionary 創造一本英漢辭典，加入五個英文單字 (key)及其對應的中文字詞(value)
#若有的英文單字有多種中文意義，請用適當的資料型態來更新並存放多種中文字詞
#再加入五個英文單字及其對應翻譯字詞
#印出本字典收納多少英文字，並以字母順序排序方式印出整本字典(可能需使用迴圈)


#dict{鍵key:值value}
dict1 = {"Takahashi Shouko":"高橋聖子","Fukada Eimi":"深田詠美","Kawakita Saika":"河北彩花","Honjō Suzu":"本庄鈴","Asuka Kirara":"明日花綺羅"}

dict2 = {"Miku Ohashi":"大橋未久","Momonogi Kana":"桃乃木香奈","Mikami Yua":"三上悠亞","	Amatsuka Moe":"天使萌","Uehara Ai":"上原亞衣",}

dict3 = {"leave":["留下","離開"], "if":["如果","是否"]}
#
#dictionary無法相加
#利用.update合併 由dict1執行
dict1.update(dict2)
dict1.update(dict3)


#印出排序後的dict1一共多少英文單字 #一共是10個單字
print("英文單字數量為",len(dict1))

#歸零計數器
english_word_count = 0

#計算出這個字典裡有多少英文字
for key in dict1:
   # += 讓a=a+b
   english_word_count +=len(key)

print("一共有",english_word_count,"個字")


#排列dict1中的鍵
sorted_dict = sorted(dict1.items())
#排列之後 再進行迴圈
for key,value in sorted_dict:
    print(key,":",value)