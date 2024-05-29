#找出從2~1000為質數之數字，把所有質數存入一個list，並輸出至螢幕。如[2,3,5,7,11,13,17,...]

list = []

for i in range(2,1001):
    prime_number = True #假設布林值之質數為真(二度確認)
    for j in range(2,i): #當j 在2至(2到1000的範圍) 
        if i % j == 0 : # 如果i除j 餘數比較是否為0
            prime_number = False #則不是質數
            break       #接著中斷
    if prime_number: #回到上層迴圈 如果是質數
        list.append(i) #則將該質數加入到列表中

print(list)
            