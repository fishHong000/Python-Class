def main():
    n = int(input()) # 第一個輸入表示有幾筆資料
    got = 0 # 已經處理幾個數字
    sum = 0 # 所有已讀入數字的和
    while got < n: # 當還有數字需要處理
        sum = sum + int(input()) # 加總
        got = got + 1 # 記得多處理了一筆資料
    print(sum)

if __name__ == "__main__" :
    main()