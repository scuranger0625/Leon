#自檔案開始一次讀一個字元並顯示於螢幕，直到讀取完全部檔案。
#自檔案開始一次讀一個字元並顯示於螢幕，如果讀取到的文字為英文小寫，轉換成大寫再印出，直到讀取完全部檔案。
#自檔案開始讀取一行一行文字並顯示於螢幕，直到讀取完全部檔案。
#自檔案開始讀取一行一行文字並顯示於螢幕，如果讀取到的文字為 台灣，轉換成  臺灣  再印出，直到讀取完全部檔案。
with open(r"C:\Users\Leon\Desktop\python\讀取文本練習檔案\text.txt.txt",'r',encoding='utf-8') as file:
    while True:  #進入無限迴圈
        char = file.read(1) #方法讀取文件中的下一個字元，並將其存儲在 char 變數中。
        if not char: #如果 char 為空，表示已經到達文件的結尾，則退出迴圈。
            break
        print(char)

with open(r"C:\Users\Leon\Desktop\python\讀取文本練習檔案\text.txt.txt",'r',encoding='utf-8') as file:
    while True:
        char = file.read(1)
        if not char:
            break   #跳出while或for
        if char.islower():   #.islower()檢查是否為小寫字母
            char = char.upper()  #.upper將所有轉換成大寫字母
        print(char)

with open(r"C:\Users\Leon\Desktop\python\讀取文本練習檔案\text.txt.txt",'r',encoding='utf-8') as file:
    for line in file:
        print(line)

with open(r"C:\Users\Leon\Desktop\python\讀取文本練習檔案\text.txt.txt", 'r', encoding='utf-8') as file:
    
    #line 通常指的是一個文本文件中的一行文字。在 Python 中，特別是在處理文件時，我們常常使用 line 來代表從文件中讀取的一行文字。
    for line in file:
        #.replace替換字符串中的一個子串為另一個指定的字符串
        line = line.replace("台灣", "臺灣")  
        print(line)










