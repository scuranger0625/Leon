import random

class TaiwanIDGenerator:
    def __init__(self):
        self.area_codes = {'台北市': 'A', '台中市': 'B', '基隆市': 'C', '台南市': 'D', '高雄市': 'E', '新北市': 'F',
                           '宜蘭縣': 'G', '桃園市': 'H', '新竹縣': 'J', '苗栗縣': 'K', '台中縣': 'L', '南投縣': 'M',
                           '彰化縣': 'N', '雲林縣': 'P', '嘉義縣': 'Q', '台南縣': 'R', '高雄縣': 'S', '屏東縣': 'T',
                           '花蓮縣': 'U', '台東縣': 'V', '澎湖縣': 'X', '陽明山': 'Y', '金門縣': 'W', '連江縣': 'Z',
                           '嘉義市': 'I', '新竹市': 'O'}
        self.area_nums = {'台北市': 10, '台中市': 11, '基隆市': 12, '台南市': 13, '高雄市': 14, '新北市': 15,
                          '宜蘭縣': 16, '桃園市': 17, '新竹縣': 34, '苗栗縣': 18, '台中縣': 19, '南投縣': 21,
                          '彰化縣': 22, '雲林縣': 32, '嘉義縣': 20, '台南縣': 23, '高雄縣': 24, '屏東縣': 27,
                          '花蓮縣': 28, '台東縣': 29, '澎湖縣': 30, '陽明山': 31, '金門縣': 33, '連江縣': 35,
                          '嘉義市': 25, '新竹市': 26}


    def calculate_possible_ids(self):
        gender_list = [1, 2, 8, 9]
        random_digits_count = 10 ** 7
        total_ids_count = len(self.area_codes) * len(gender_list) * random_digits_count
        return total_ids_count

    def generate(self, city, gender):
        if city not in self.area_codes or gender not in [1, 2, 8, 9]:
            raise ValueError("Invalid city or gender.")
        
        area_code = self.area_codes[city]
        area_num = self.area_nums[city]

        for _ in range(10):
            random_digits = [random.randint(0, 9) for _ in range(7)]
            id_without_checksum = [area_num // 10, area_num % 10, gender] + random_digits
            checksum = self.calculate_checksum(id_without_checksum)
            id_number = f"{area_code}{gender}{''.join(map(str, random_digits))}{checksum}"
            yield id_number

    def calculate_checksum(self, id_digits):
        weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        weighted_sum = sum(d * w for d, w in zip(id_digits, weights))
        checksum = (10 - (weighted_sum % 10)) % 10
        return checksum

# 主程式
generator = TaiwanIDGenerator()
total_ids_count = generator.calculate_possible_ids()

print(f"預計產生 {total_ids_count} 個全台縣市身份證字號")

while True:
    city = input("請輸入縣市名稱：")
    gender = int(input("請輸入性別碼 (1: 男性, 2: 女性, 8: 歸化男性, 9: 歸化女性)："))

    try:
        for id_number in generator.generate(city, gender):
            print(id_number)
        break  # 跳出迴圈
    except ValueError as e:
        print(e)





    

