def find(name,card):
    if sum(card) == 0:
        return
    # 找眼
    if sum(card) == 17:
        for i in range(34):
            if card[i] == 2:
                card[i] = 0
                sum(card)-2


def main():
    card = list(map(int,input().split()))
    name = ['一萬','二萬','三萬','四萬','五萬','六萬','七萬','八萬','九萬',\
            '一筒','二筒','三筒','四筒','五筒','六筒','七筒','八筒','九筒',\
            '一條','二條','三條','四條','五條','六條','七條','八條','九條',\
            '東','南','西','北','中','發','白']
    find(name,card)

if __name__ == '__main__':
    main()