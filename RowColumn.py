# 1. how many rows? max(data+2)
# 2. how many columns? n
# row from max(data)+2 ~ 1
# 3. for any r,c print what?
# '##' if data[c] >= line
# '..' if data[c] < line

def printGraph(n, height):
    for r in range(max(height)+2,0,-1):
        print(str(r).rjust(2,'0'), end=' ')
        for c in range(n):
            if height[c]>=r:
                print('##', end=' ')
            else:
                print('..', end=' ')
        print()
    for c in range(n+1):
        print(str(c).rjust(2,'0'), end=' ')

def main():
    n = int(input())
    height = list(map(int,input().split()))
    printGraph(n, height)

if __name__ == '__main__':
    main()