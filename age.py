def main():
    # 輸入年齡, int
    age = int(input())
    # 依據年齡印出小孩,成年,或老頭
    if age < 18 :
        print("小孩")
    elif age < 60 :
        print("成年")
    else :
        print("老頭")
if __name__ == "__main__" :
    main()