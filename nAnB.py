# 玩過猜數字的遊戲吧
# 猜4個數字
# 由0~9組成, 不重複
# 猜對方的數字, 被猜的要回答?A?B
# A代表有這個數字且位置一樣,B代表有這個數字,但位置不對
# eg, 秘密數字是1357(X), 猜Y=0123, 要回答0A2B
# 0123可能是解嗎? no
# 0124可能是解嗎? no
# 1357可能是解嗎? yes
# 2058可能是解嗎? yes
# 請寫一個程式猜你的祕密數字
# 提示: 消去法
# 比對x,y傳回幾A幾B
def nAnB(x,y):
    a,b = 0,0
    for num in x: # 對每一個X裡的數字
        if num in y: # 有A或B
            if x.index(num) == y.index(num):
                a = a + 1
            else:
                b = b + 1
    return[a,b]
# sol: 所有可能的數字
# y: 電腦猜的數字
# r: 人類的回應
# 傳回消掉不可能解後的sol子集合
def delete(sol,y,r):
    result = []
    for num in sol:
        if nAnB(num,y) == r:
            result.append(num)
    return result

def main():
    # 先產生所有的可能解,10*9*8*7
    # 先亂猜一個數字
    myGuess = 
    # 印出猜的數字
    print(*myGuess)
    while True:
        response = list(map(input().split()))
        if reponse == [4,0]:
            return
        # 根據response, 把不可能的解去掉
        # 秘密解為X, 得到回應reponse, 那可能的解y必定和X比對結果是response
        # 再亂猜一個數字
        myGuess = choose(?)
        print(*myGuess)

if __main__ == '__name__':
    main()