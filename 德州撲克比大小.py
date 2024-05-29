import random

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

# 兩個玩家各自抽取五張牌
player1 = draw_cards(poker, 5)
player2 = draw_cards(poker, 5)

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
            return "High card", 0  # 默認為高牌

    @staticmethod
    def compare_highcard(hand1, hand2):
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
            return "High card", 0  # 默認為高牌

    @staticmethod
    def compare_highcard(hand1, hand2):
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

# 顯示每位玩家的牌以及牌型
for i, player_hand in enumerate(players, start=1):
    print(f"Player {i} Hand:", player_hand, "(", detect_hand_type(player_hand), ")")

# 比較玩家手牌大小
winners = []
max_strength = float('-inf')  # 設置初始的最大強度值為負無窮大
for i, player_hand in enumerate(players, start=1):
    strength = PokerHandComparator.get_hand_type(player_hand)[1]  # 獲取牌型的強度
    if strength > max_strength:
        winners = [i]  # 如果有更強的牌型，則更新勝利者列表
        max_strength = strength
    elif strength == max_strength:
        winners.append(i)  # 如果有多個牌型強度相同，則都加入勝利者列表

if len(winners) == 1:
    print("Player", winners[0], "wins!")
else:
    print("It's a tie between players", ", ".join(map(str, winners)) + "!")

def compare_hands(players):
    winners = []
    max_strength = -1
    
    for i, hand in enumerate(players):
        hand_type, hand_strength = PokerHandComparator.get_hand_type(hand)
        
        if hand_strength > max_strength:
            winners = [i]
            max_strength = hand_strength
        elif hand_strength == max_strength:
            winners.append(i)
    
    return winners


def compare_all_hands(players):
    winners = []
    max_strength = -1
    
    for i, hand in enumerate(players):
        hand_type, hand_strength = PokerHandComparator.get_hand_type(hand)
        
        if hand_strength > max_strength:
            winners = [i]
            max_strength = hand_strength
        elif hand_strength == max_strength:
            winners.append(i)
    
    return winners

# 在比較玩家手牌大小之前，找到手牌中最強的牌型
winners = compare_all_hands(players)

# 印出結果
if len(winners) == 1:
    print("Player", winners[0], "wins with the strongest hand!")
else:
    print("It's a tie between players", ", ".join(map(str, winners)), "with the same strongest hand!")







