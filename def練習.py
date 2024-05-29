#請撰寫以下三個函數，這些函數可以傳入list或tuple的數值參數，並計算回傳:
#average(....):平均數
#st_dev(....):標準差
#median(....):中位數

import statistics

import random

# 產生包含 20 個隨機正數的列表
positive_numbers = [random.randint(1, 100) for _ in range(20)]

positive_numbers = sorted(positive_numbers)

total = sum(positive_numbers)

#A = positive_numbers[0:21]

print(positive_numbers)
print(total)


#average接受名為total的參數，此時會被定義為返回計算total/列表的總長度
def average(total):
    return total / len (positive_numbers)
print("平均數為", average(total))

#計算標準差
def st_dev(positive_numbers):
    avg = average(total)
    variance =sum((i-avg)**2 for i in positive_numbers)/len(positive_numbers)
    return variance**0.5
print("標準差為", st_dev(positive_numbers))

#計算中位數 由於list的長度固定為20 因此會是list中的第10個數字和第11個數字的加總除2
def median(positive_numbers):
    return (positive_numbers[9] + positive_numbers[10])/2
print("中位數為",median(positive_numbers))

#請撰寫函數，傳入兩個正整數，傳回此二數的:
#最大公因數
#最小公倍數

#Hint:用程式實作輾轉相除法