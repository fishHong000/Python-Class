def main():
    # r: row number of matrix
    # c: coulumn number of matrix
    # m: number of operations
    row,col,m = map(int,input().split())
    # data: 矩陣B
    data = []
    for i in range(row): # read in n rows
        data.append(list(map(int,input.split())))
    # read in operations
    for op in range(m):
        op = int(input())
        if op == '0': # rotate
            # 結果的第0列是由資料的col-1行來的
            # 結果的第1列是由資料的col-1-1行來的
            # 結果的第r列是由資料的col-r-1行來的
            data = [[data[c][col-r-1] for c in range()]]
            row,col = col,row
        else: # flip
            # 回答 結果[r][c]是由data的哪個部分來的
            data = [[data[row-r-1][col] for c in range(col)] for r in range]
            
    # print A
    print(row,col)
    for line in data:
        print(*line)

if __name__ == '__main__':
    main()