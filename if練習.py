#每4年一潤,100年不潤,400年一潤



#製造等差數列
start = 1900
end = 2100
step = 4

years = [start + i * step for i in range((end - start) // step + 1)]


#year雖並沒有被定義,但在for year in years:這句話當中 year被定義成迴圈years的每一個數


for year in years:
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print(year,"是閏年")
    else:
        print(year,"不是閏年")