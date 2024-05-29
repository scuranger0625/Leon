import random

poker_hand_strength = {
    "High card": 0,
    "One pair": 1,
    "Two pair": 2,
    "Three of a kind": 3,
    "Straight": 4,
    "Flush": 5,
    "Full house": 6,
    "Four of a kind": 7,
    "Straight flush": 8
}

# 定義四個花色的撲克牌列表
spades = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
hearts = ['A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥']
diamonds = ['A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
clubs = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']

# 將四個花色的列表合併成一副撲克牌
poker = spades + hearts + diamonds + clubs

# 定義一個函數來隨機抽取指定數量的牌
def draw_cards(deck, quantity):
    return random.sample(deck, quantity)

# 定義一個函數來初始化玩家手牌
def init_players(num_players):
    players = []
    for _ in range(num_players):
        player_hand = draw_cards(poker, 5)  # 每位玩家抽取五張牌
        players.append(player_hand)
    return players

# 玩家各自抽取五張牌
num_players = int(input("Enter the number of players (2-4): "))  # 讓玩家輸入欲參與的玩家數量
if num_players < 2 or num_players > 4:
    print("Invalid number of players. Please enter a number between 2 and 4.")
else:
    players = init_players(num_players)


class Straightflush: #定義種類:同花順
    def __init__(self, cards):
        self.cards = cards

    def is_straight_flush(self):
        # 檢查牌是否是同一花色
        suits = {card[-1] for card in self.cards}
        if len(suits) != 1:  #檢查花色的種類是否為1 !=1表示不等於1
            return False
        
        # 檢查牌是否連續
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        sorted_values = sorted([values[card[:-1]] for card in self.cards])
        for i in range(4):
            if sorted_values[i] + 1 != sorted_values[i + 1]:
                return False
        
        return True

class Fourofakind: #定義種類:鐵支
    def __init__(self, cards):
        self.cards = cards

    def is_four_of_a_kind(self):
        # card[:-1]: 對於每張牌，使用切片操作 [:-1] 提取牌的前面部分，即去除花色部分，只保留點數部分。例如，將 '10♠' 切片為 '10'。
        # for card in self.cards: 迭代 self.cards 中的每一張牌
        values = [card[:-1] for card in self.cards]
        # 將點數和其出現次數作為鍵值對，通過字典推導式生成一個字典，其中點數是鍵，該點數在牌組中出現的次數是值。
        value_counts = {value: values.count(value) for value in values}
        if 4 in value_counts.values():
            return True
        return False

class Fullhouse: #定義種類:葫蘆
    def __init__(self, cards):
        self.cards = cards

    def is_full_house(self):
         # card[:-1]: 對於每張牌，使用切片操作 [:-1] 提取牌的前面部分，即去除花色部分，只保留點數部分。例如，將 '10♠' 切片為 '10'。
         # for card in self.cards: 迭代 self.cards 中的每一張牌
        values = [card[:-1] for card in self.cards]
         # 將點數和其出現次數作為鍵值對，通過字典推導式生成一個字典，其中點數是鍵，該點數在牌組中出現的次數是值。
        value_counts = {value: values.count(value) for value in values}
        if 2 in value_counts.values() and 3 in value_counts.values():
            return True
        return False

class Flush:  #定義種類 同花
    def __init__(self, cards):
        self.cards = cards

    def is_flush(self):
        suits = {card[-1] for card in self.cards}
        if len(suits) == 1:  #如果花色只有一種
            return True
        return False
    
class Straight: #定義種類 順子
    def __init__(self, cards):
        self.cards = cards

    def is_straight(self):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        #將每張牌的點數依次提取出來，並且根據 values 字典將點數轉換為對應的數值，存儲在一個列表中。
        # card[:-1] 切片成數字
        sorted_values = sorted([values[card[:-1]] for card in self.cards])
        
        # 檢查是否連續
        for i in range(4):
            if sorted_values[i] + 1 != sorted_values[i + 1]:
                return False
        
        return True

class Threeofakind:  #定義三條
    def __init__(self, cards):
        self.cards = cards

    def is_three_of_a_kind(self):
        values = [card[:-1] for card in self.cards]
        value_counts = {value: values.count(value) for value in values} #.count(value) 是列表方法，用於計算列表中某個元素出現的次數。
        
        #.values() 是字典方法，用於獲取字典中所有的值。
        if 3 in value_counts.values():  
            return True
        return False

class Twopair:  #定義兩對
    def __init__(self, cards):
        self.cards = cards

    def is_two_pair(self):
        values = [card[:-1] for card in self.cards]
        value_counts = {value: values.count(value) for value in values}
        pairs = 0
        for count in value_counts.values():
            #在迴圈內部，對於每個值，程式檢查是否等於 2。
            #如果某個點數在牌組中出現了兩次，則將 pairs 變數加一。這樣，pairs 變數將記錄牌組中點數出現兩次的次數。
            if count == 2:  
                pairs += 1

        #在迴圈之後，程式檢查 pairs 變數是否等於 2。如果有兩對點數相同的牌，pairs 變數的值將為 2，此時返回 True，表示牌組是兩對。
        if pairs == 2:
            return True
        return False

class Onepair: #定義一對
    def __init__(self, cards):
        self.cards = cards

    def is_one_pair(self):
        values = [card[:-1] for card in self.cards]
        value_counts = {value: values.count(value) for value in values}
        if 2 in value_counts.values():  #.values()獲取字典內的值是否為相同的數字
            return True
        return False

class Highcard: #定義高牌
    def __init__(self, cards):
        self.cards = cards

    def is_high_card(self):
        values = [card[:-1] for card in self.cards]
        highest_value = max(values, key=lambda x: values.index(x))  # 找到牌組中最高的點數
        return highest_value


# 定義一個函數來隨機抽取指定數量的牌
def draw_cards(deck, quantity):
    return random.sample(deck, quantity)

# 最多4個玩家各自抽取五張牌
player1 = draw_cards(poker, 5)
player2 = draw_cards(poker, 5)
player3 = draw_cards(poker, 5)
player4 = draw_cards(poker, 5)


#判斷玩家手上的牌型
def detect_hand_type(hand):
    if Straightflush(hand).is_straight_flush():
        return "Straight flush"
    elif Fourofakind(hand).is_four_of_a_kind():
        return "Four of a kind"
    elif Fullhouse(hand).is_full_house():
        return "Full house"
    elif Flush(hand).is_flush():
        return "Flush"
    elif Straight(hand).is_straight():
        return "Straight"
    elif Threeofakind(hand).is_three_of_a_kind():
        return "Three of a kind"
    elif Twopair(hand).is_two_pair():
        return "Two pair"
    elif Onepair(hand).is_one_pair():
        return "One pair"
    else:
        return "High card"


class PokerHandComparator:
    @staticmethod
    def compare(hand1, hand2):
        # 定義牌型的強度，按照常見撲克牌規則，從最弱到最強
        poker_hand_strength = {
            "High card": 0,
            "One pair": 1,
            "Two pair": 2,
            "Three of a kind": 3,
            "Straight": 4,
            "Flush": 5,
            "Full house": 6,
            "Four of a kind": 7,
            "Straight flush": 8
        }

        # 獲取牌型和牌型的強度
        hand1_type, hand1_strength = PokerHandComparator.get_hand_type(hand1)
        hand2_type, hand2_strength = PokerHandComparator.get_hand_type(hand2)

        # 如果牌型不同，則直接根據強度比較
        if hand1_type != hand2_type:
            return poker_hand_strength[hand1_type] - poker_hand_strength[hand2_type]

        # 如果牌型相同，則需要比較特定牌型的大小
        if hand1_strength != hand2_strength:
            return hand1_strength - hand2_strength

        # 如果牌型和強度都相同，則比較高牌的大小
        return PokerHandComparator.compare_highcard(hand1, hand2)

    @staticmethod
    def get_hand_type(hand):
        # 根據牌組的具體情況，返回對應的牌型和牌型的強度
        if Straightflush(hand).is_straight_flush():
            return "Straight flush", 8
        elif Fourofakind(hand).is_four_of_a_kind():
            return "Four of a kind", 7
        elif Fullhouse(hand).is_full_house():
            return "Full house", 6
        elif Flush(hand).is_flush():
            return "Flush", 5
        elif Straight(hand).is_straight():
            return "Straight", 4
        elif Threeofakind(hand).is_three_of_a_kind():
            return "Three of a kind", 3
        elif Twopair(hand).is_two_pair():
            return "Two pair", 2
        elif Onepair(hand).is_one_pair():
            return "One pair", 1
        else:
            return "High card", Highcard(hand).is_high_card()

    @staticmethod
    def compare_highcard(hand1, hand2):
        # 比較兩組手牌中最高點數的牌
        high_card1 = Highcard(hand1).is_high_card()
        high_card2 = Highcard(hand2).is_high_card()

        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        if values[high_card1] > values[high_card2]:
            return 1
        elif values[high_card1] < values[high_card2]:
            return -1
        else:
            return 0
        
class StraightFlushComparator:  #比較同花順大小
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 將每個玩家的牌按照點數由大到小排序
        sorted_hand1 = sorted([values[card[:-1]] for card in hand1], reverse=True)
        sorted_hand2 = sorted([values[card[:-1]] for card in hand2], reverse=True)

        # 比較順子中最大的數字
        max_value_hand1 = max(sorted_hand1)
        max_value_hand2 = max(sorted_hand2)

        # 如果兩個順子的最大數字不同，則返回比較結果
        if max_value_hand1 != max_value_hand2:
            return max_value_hand1 - max_value_hand2

        # 如果最大數字相同，則是平局
        return 0

class FourOfAKindComparator: #比較鐵支大小
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 將每個玩家的牌按照點數由大到小排序
        sorted_hand1 = sorted([values[card[:-1]] for card in hand1], reverse=True)
        sorted_hand2 = sorted([values[card[:-1]] for card in hand2], reverse=True)

        # 找到每個玩家手中的鐵支點數和單張點數
        unique_value_hand1 = set(sorted_hand1)
        unique_value_hand2 = set(sorted_hand2)

        # 比較鐵支的點數
        four_of_a_kind_value_hand1 = [value for value in unique_value_hand1 if sorted_hand1.count(value) == 4][0]
        four_of_a_kind_value_hand2 = [value for value in unique_value_hand2 if sorted_hand2.count(value) == 4][0]

        # 如果兩個鐵支的點數不同，則返回比較結果
        if four_of_a_kind_value_hand1 != four_of_a_kind_value_hand2:
            return four_of_a_kind_value_hand1 - four_of_a_kind_value_hand2

        # 如果鐵支的點數相同，則比較單張的大小
        single_hand1 = [value for value in unique_value_hand1 if sorted_hand1.count(value) == 1][0]
        single_hand2 = [value for value in unique_value_hand2 if sorted_hand2.count(value) == 1][0]

        return single_hand1 - single_hand2
    
class FullHouseComparator: #比較葫蘆大小
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 將每個玩家的牌按照點數由大到小排序
        sorted_hand1 = sorted([values[card[:-1]] for card in hand1], reverse=True)
        sorted_hand2 = sorted([values[card[:-1]] for card in hand2], reverse=True)

        # 找到每個玩家手中的三條點數和對子點數
        unique_value_hand1 = set(sorted_hand1)
        unique_value_hand2 = set(sorted_hand2)

        three_of_a_kind_value_hand1 = [value for value in unique_value_hand1 if sorted_hand1.count(value) == 3][0]
        three_of_a_kind_value_hand2 = [value for value in unique_value_hand2 if sorted_hand2.count(value) == 3][0]

        # 比較三條的點數
        if three_of_a_kind_value_hand1 != three_of_a_kind_value_hand2:
            return three_of_a_kind_value_hand1 - three_of_a_kind_value_hand2

        # 如果三條的點數相同，則比較對子的大小
        pair_value_hand1 = [value for value in unique_value_hand1 if sorted_hand1.count(value) == 2][0]
        pair_value_hand2 = [value for value in unique_value_hand2 if sorted_hand2.count(value) == 2][0]

        return pair_value_hand1 - pair_value_hand2

class FlushComparator:
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 將每個玩家的牌按照點數由大到小排序
        sorted_hand1 = sorted([values[card[:-1]] for card in hand1], reverse=True)
        sorted_hand2 = sorted([values[card[:-1]] for card in hand2], reverse=True)

        # 逐一比較每個點數的大小
        for card1, card2 in zip(sorted_hand1, sorted_hand2):
            if card1 != card2:
                return card1 - card2

        # 如果所有牌的點數都相同，則返回0表示平局
        return 0

class StraightComparator:
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 將每個玩家的牌按照點數由大到小排序
        sorted_hand1 = sorted([values[card[:-1]] for card in hand1], reverse=True)
        sorted_hand2 = sorted([values[card[:-1]] for card in hand2], reverse=True)

        # 比較最大點數
        max_card1 = max(sorted_hand1)
        max_card2 = max(sorted_hand2)

        if max_card1 != max_card2:
            return max_card1 - max_card2

        # 如果最大點數相同，則比較最小點數
        min_card1 = min(sorted_hand1)
        min_card2 = min(sorted_hand2)

        return min_card1 - min_card2

class ThreeOfAKindComparator:
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 取得每個玩家的牌的點數列表
        hand1_values = [values[card[:-1]] for card in hand1]
        hand2_values = [values[card[:-1]] for card in hand2]

        # 找出每個玩家的三條牌的點數
        hand1_triple = max(set(hand1_values), key=hand1_values.count)
        hand2_triple = max(set(hand2_values), key=hand2_values.count)

        # 比較三條牌的點數
        if hand1_triple != hand2_triple:
            return hand1_triple - hand2_triple

        # 如果三條牌的點數相同，則比較剩餘兩張牌的大小
        hand1_remain = [value for value in hand1_values if value != hand1_triple]
        hand2_remain = [value for value in hand2_values if value != hand2_triple]

        # 將剩餘兩張牌排序
        hand1_remain.sort(reverse=True)
        hand2_remain.sort(reverse=True)

        # 比較剩餘兩張牌的大小
        for card1, card2 in zip(hand1_remain, hand2_remain):
            if card1 != card2:
                return card1 - card2

        # 如果剩餘兩張牌都相同，則是平局
        return 0

class TwoPairComparator:
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 取得每個玩家的牌的點數列表
        hand1_values = [values[card[:-1]] for card in hand1]
        hand2_values = [values[card[:-1]] for card in hand2]

        # 找出每個玩家的兩對牌的點數
        hand1_pairs = [value for value in set(hand1_values) if hand1_values.count(value) == 2]
        hand2_pairs = [value for value in set(hand2_values) if hand2_values.count(value) == 2]

        # 將兩對牌的點數排序
        hand1_pairs.sort(reverse=True)
        hand2_pairs.sort(reverse=True)

        # 比較第一對牌的大小
        if hand1_pairs[0] != hand2_pairs[0]:
            return hand1_pairs[0] - hand2_pairs[0]

        # 比較第二對牌的大小
        if hand1_pairs[1] != hand2_pairs[1]:
            return hand1_pairs[1] - hand2_pairs[1]

        # 如果兩對牌的大小都相同，則比較剩餘的單張牌的大小
        hand1_remain = [value for value in hand1_values if value not in hand1_pairs]
        hand2_remain = [value for value in hand2_values if value not in hand2_pairs]

        # 將剩餘的單張牌排序
        hand1_remain.sort(reverse=True)
        hand2_remain.sort(reverse=True)

        # 比較剩餘的單張牌的大小
        for card1, card2 in zip(hand1_remain, hand2_remain):
            if card1 != card2:
                return card1 - card2

        # 如果剩餘的單張牌都相同，則是平局
        return 0

class OnePairComparator:
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 取得每個玩家的牌的點數列表
        hand1_values = [values[card[:-1]] for card in hand1]
        hand2_values = [values[card[:-1]] for card in hand2]

        # 找出每個玩家的一對牌的點數
        hand1_pair = [value for value in set(hand1_values) if hand1_values.count(value) == 2][0]
        hand2_pair = [value for value in set(hand2_values) if hand2_values.count(value) == 2][0]

        # 如果兩個玩家的一對牌的點數不同，則較大的點數的一對牌贏
        if hand1_pair != hand2_pair:
            return hand1_pair - hand2_pair

        # 如果一對牌的點數相同，則比較剩餘的單張牌的大小
        hand1_remain = [value for value in hand1_values if value != hand1_pair]
        hand2_remain = [value for value in hand2_values if value != hand2_pair]

        # 將剩餘的單張牌排序
        hand1_remain.sort(reverse=True)
        hand2_remain.sort(reverse=True)

        # 比較剩餘的單張牌的大小
        for card1, card2 in zip(hand1_remain, hand2_remain):
            if card1 != card2:
                return card1 - card2

        # 如果剩餘的單張牌都相同，則是平局
        return 0

class HighCardComparator:
    @staticmethod
    def compare(hand1, hand2):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # 取得每個玩家的牌的點數列表
        hand1_values = [values[card[:-1]] for card in hand1]
        hand2_values = [values[card[:-1]] for card in hand2]

        # 將每個玩家的牌的點數列表按照大小排序
        hand1_values.sort(reverse=True)
        hand2_values.sort(reverse=True)

        # 比較排序後的每個玩家的牌
        for card1, card2 in zip(hand1_values, hand2_values):
            if card1 != card2:
                return card1 - card2

        # 如果所有牌都相同，則是平局
        return 0

# 計算每個玩家手牌的牌型
hand_types = [(i, detect_hand_type(players[i])) for i in range(num_players)]

# 找到最強的牌型
max_hand_type = max(hand_types, key=lambda x: poker_hand_strength.get(x[1], 0))

# 找到所有擁有最強牌型的玩家
winners = [player for player, hand_type in hand_types if hand_type == max_hand_type[1]]



# 如果只有一位玩家擁有最強牌型，則該玩家勝出
if len(winners) == 1:
    print(f"Player {winners[0] + 1} wins with {max_hand_type[1]}!")

# 如果有多位玩家擁有最強牌型，則進一步比較他們的牌型強度
else:
    # 將所有最強牌型的玩家的手牌按照牌型強度進行排序
    sorted_winners = sorted(winners, key=lambda x: PokerHandComparator.get_hand_type(players[x])[1], reverse=True)
    # 如果只有兩位玩家，則直接比較他們的手牌
    if len(sorted_winners) == 2:
        result = PokerHandComparator.compare(players[sorted_winners[0]], players[sorted_winners[1]])
        if result == 1:
            print(f"Player {sorted_winners[0] + 1} wins with {max_hand_type[1]}!")
        elif result == -1:
            print(f"Player {sorted_winners[1] + 1} wins with {max_hand_type[1]}!")
        else:
            print(f"It's a tie between players {sorted_winners[0] + 1} and {sorted_winners[1]}.")
    # 如果有多位玩家，則進一步比較他們的手牌
    else:
        # 找到最強牌型的玩家的手牌強度
        max_strength = PokerHandComparator.get_hand_type(players[sorted_winners[0]])[1]
        # 找到所有手牌強度和最強牌型相同的玩家
        equal_strength_players = [player for player in sorted_winners if PokerHandComparator.get_hand_type(players[player])[1] == max_strength]
        # 如果只有一位玩家，則該玩家勝出
        if len(equal_strength_players) == 1:
            print(f"Player {equal_strength_players[0] + 1} wins with {max_hand_type[1]}!")
        # 如果有多位玩家，則宣布平局
        else:
            print(f"It's a tie between players {', '.join(str(player + 1) for player in equal_strength_players)} with the same strongest hand!")

# 顯示每位玩家的牌以及牌型
for i, player_hand in enumerate(players, start=1):
    hand_type = detect_hand_type(player_hand)
    print(f"Player {i} Hand:", player_hand, "(", hand_type, ")")
