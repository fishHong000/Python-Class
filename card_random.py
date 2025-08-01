# 108213010 洪瑄妤
# 產生牌
# 洗牌
# 發牌
# 整理牌
# 印牌
import random

def printCard(hand):
    # 建立需要印的東西的list 
    colors = ['S','H','D','C']
    num = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    # num 
    for i in range(4): # 印color
        print(colors[i] , end = ' ')
        for j in range(13): # 把hand印出來
        # 檢查每張牌的花色
        # 再印num
            if hand[j]//13 == i: # 手上的13張牌去印
                print(num[hand[j]%13],end = '')
        print() # 換行
def distribute(cards):
    players = ['North','East','South','West']
    # 一次發一個人的牌
    # 總共發四次，用for來做
    for i in range(4):
        hand = cards[i*13:i*13+13] # 發牌 [0:13] [13:26] [26:39] [39:52]
        # 先印player
        print(players[i]+':') #+表示沒空格
        # 整理
        hand.sort() 
        printCard(hand)

def main():
    # 產生牌，用cards的list存
    cards = [ i for i in range(52) ] #52張牌
    # 洗牌
    random.shuffle(cards)
    # 發牌 distribute(cards)
    distribute(cards)
    
if __name__ == '__main__' :
    main()
    main()