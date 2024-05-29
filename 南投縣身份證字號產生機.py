 #若你在南投縣戶政機關擔任程式設計師，你被指派去撰寫南投縣民身份證字號產生器，請利用Python 中 iterator 或 generator  function 實作
 #呼叫 next() 時，該產生器會 ”依序” 產生”合乎驗證公式”的南投縣民身份證字號
 #若產生器若已產生完所有合乎驗證公式身分證字號，將擲出 StopIteration
 #主程式中，請依序印出所有合乎驗證公式”的南投縣民身份證字號
 #提示，使用 while 或 for 迴圈

import itertools
import random
import time

class NantouIDGenerator:
    def __init__(self):
        self.area_code = 'M'
        self.area_num = 21

    def calculate_possible_ids(self):
        gender_list = [1,2,8,9]
        random_digits_count = 10 ** 7
        area_code_count = 1  
        gender_random_combinations_count = len(gender_list) * random_digits_count
        total_ids_count = area_code_count * gender_random_combinations_count
        return total_ids_count

    def generate(self):
        for gender in [1,2,8,9]:
            for _ in range(10):  # 這裡改成迭代10次，以生成10個不同的隨機數字
                random_digits = [random.randint(0, 9) for _ in range(7)]  # 每次生成7位不同的隨機數字
                id_without_checksum = [self.area_num // 10, self.area_num % 10, gender] + random_digits
                checksum = self.calculate_checksum(id_without_checksum)
                id_number = f"{self.area_code}{gender}{''.join(map(str, random_digits))}{checksum}"
                yield id_number

    def calculate_checksum(self, id_digits):
        weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        weighted_sum = sum(d * w for d, w in zip(id_digits, weights))
        checksum = (10 - (weighted_sum % 10)) % 10
        return checksum

# 主程式
generator = NantouIDGenerator()
total_ids_count = generator.calculate_possible_ids()

print(f"預計產生 {total_ids_count} 個南投縣身份證字號")

while True:
    choice = input("請選擇：1. 生成一個身份證字號；2. 生成所有身份證字號；3. 結束：")
    
    if choice == '1':
        print(next(generator.generate()))
    elif choice == '2':
        for id_number in generator.generate():
            print(id_number)
    elif choice == '3':
        print("結束程式。")
        break
    else:
        print("請輸入有效選項。")



    

