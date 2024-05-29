#有A、B、C三人，A、B兩人想知道C的生日
#C便給他們出了一道謎題:
#C首先在紙上列出幾組日期，並告知其中一組就是答案 5/15,5/16,5/19,6/17,6/18,7/14,7/16,8/14,8/15,8/17
#C告訴A生日月份，但A不知道日期
#C告訴B生日日期，但B不知道月份


#A表示:我不知道C的生日，但我確定B也不知道
#B表示:我原本也不知道C的生日，但我現在知道了
#A表示:那我也知道了
#請問C的生日是哪一組?

X = 7
Y = 16
Z = [X, Y]

A_known_month_input = input("請輸入生日月份：")

B_known_date_input = input("請輸入生日日期：")

idiots = [A_known_month_input,B_known_date_input]

print(idiots)


# 定義一個名為 check_answer 的函數，接受兩個參數 month 和 date
def check_answer(month, date):
    while True:
        if month < 0 or month > 12:
            print("你是個低能兒，月份必須在 1 到 12 之間")
            month = int(input("請重新輸入生日月份："))
            continue
        
        if date < 0 or date > 31:
            print("你是個低能兒，日期必須在 1 到 31 之間")
            date = int(input("請重新輸入生日日期："))
            continue
            
        if month == X and date == Y:
            print("恭喜你答對了")
        else:
            print("菜雞，你答錯了")
        break

# 確認輸入是否是整數，經由 input 輸入的會被判定成 str
check_answer(int(A_known_month_input), int(B_known_date_input))

#答案:

#首先 A之所以可以肯定B不知道 是因為如果B拿到的是18或19 拿B就一定會知道C的生日
#A之所以如此肯定B不知道 是因為A手上的月份 肯定不是5或6月所以A手上的只能是7或8月
#排除掉5.6月份 剩下的答案是7/14 7/16 8/14 8/15 8/17 這時候 B是無法確定C的生日的
#但是B在聽到A的回答之後 也得知了A手上的一定是7月或8月 但是 如果B手上拿到的是14號 他就無法確定生日是7/14還是8/14 剩下的日期是15.16.17
#所以 這時候 B因為知道了日期 所以拿到了16號的B 就能肯定C的生日是7/16
#接著 A因為知道手上拿到的是7月 所以他也得知了唯一可能的7/16