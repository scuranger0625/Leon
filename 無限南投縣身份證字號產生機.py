 #若你在南投縣戶政機關擔任程式設計師，你被指派去撰寫南投縣民身份證字號產生器，請利用Python 中 iterator 或 generator  function 實作
 #呼叫 next() 時，該產生器會 ”依序” 產生”合乎驗證公式”的南投縣民身份證字號
 #若產生器若已產生完所有合乎驗證公式身分證字號，將擲出 StopIteration
 #主程式中，請依序印出所有合乎驗證公式”的南投縣民身份證字號
 #提示，使用 while 或 for 迴圈


import itertools
import random
import time

# 開始計時
start_time = time.time()

class NantouIDGenerator:
    def __init__(self):
        self.area_code = 'M'
        self.area_num = 21

    def generate(self):
        # 性別碼：1 表示男性，2 表示女性 ,8表示歸化男性 ,9表示歸化女性
        for gender in [1,2,8,9]:
            # 生成所有可能的7位隨機數字組合
            for random_digits in itertools.product(range(10), repeat=7):
                # 將地區碼對應的數字和隨機數字組合起來計算檢查碼
                id_without_checksum = [self.area_num // 10, self.area_num % 10, gender] + list(random_digits)
                checksum = self.calculate_checksum(id_without_checksum)
                # 組合成完整的身份證號碼
                id_number = f"{self.area_code}{gender}{''.join(map(str, random_digits))}{checksum}"
                yield id_number

    def calculate_checksum(self, id_digits):
        # 加權數值
        weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1] #將身份證號碼的每一位數字與對應的加權數值進行配對，然後將它們相乘並計算總和，得到加權和。
        # 計算加權和
        weighted_sum = sum(d * w for d, w in zip(id_digits, weights))
        # 取模10得到檢查碼
        checksum = (10 - (weighted_sum % 10)) % 10 
        # 計算校驗碼，首先對加權和進行取模 10 的操作，然後將結果與 10 相減，再次對 10 取模，最後得到的結果就是校驗碼。
        return checksum

# 使用例子
generator = NantouIDGenerator().generate()

for id_number in generator:
    print(id_number)


# 結束計時
end_time = time.time()
elapsed_time = end_time - start_time
print(f"共花費 {elapsed_time:.2f} 秒")
    

