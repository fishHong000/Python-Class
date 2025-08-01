# 學號：10821310 姓名：洪瑄妤
# 發牌
# 並以花色+大小的順序列出來
# eg
# S AKQ32
# H T9
# D QT76
# C AQ
# 使用int, 0~51 來代表每一張牌
# 0 ~ 12, S
# 13 ~ 25, H
# 26 ~ 38, D
# 39 ~ 51, C
# 任一張牌x的花色可由 x//13取得,0:s,1:h,2:d,3:c
# 任一張牌x的號碼可由 x%13取得0:A,1:K,2:Q,3:J...
from random import randint
# x:[0,1) # 0到1, 包含0, 不包含1
# y:[a,b]
# a,b都是整數
# y = int((b-a+1))*x+a
# (b-a+1)*
# x : [0,b-a]
# a+int((b-a+1))*x : [a,b]
def showCards(hand):
    color = ['S','H','D','C'] # 花色
    num = ['A','K','Q','J','T','9','8','7','6','5','4','3','2'] # 大小
    for i in range(4): # 印color
        print(color[i] ,end = ' ')
        for j in range(13): # 把hands印出來
        # 檢查每張牌的花色
        # 再印num
            if hand[j]//13 == i: # 手上的13張牌去印
                print(num[hand[j]%13],end = '')
        print() # 換行

def distribute(cards):
    # 發牌
    hand = list() # ->hands = [cards[:13:],cards[13:26:],cards[26:39:],cards[39::]]
    hand.append(cards[:13:]) # 第1~13張牌
    hand.append(cards[13:26:]) # 第14~26張牌
    hand.append(cards[26:39:])
    hand.append(cards[39::])
    # 拿到牌, 要排好
    player = ['North','East','South','West']
    for i in range(4):
        hand[i].sort() # 排好順序
        print(player[i]+':') # 印出每個玩家
        showCards(hand[i])

def shuffle(cards):
    # 洗牌
    # 換牌換1000次
    for i in range(1000):
        x = randint(0,51) # random()*52
        y = randint(0,51)
        cards[x], cards[y] = cards[y], cards[x]
    distribute(cards)

def main():
    # 產生52張牌
    cards = [i for i in range(52)]
    shuffle(cards)

if __name__ == '__main__':
    main()