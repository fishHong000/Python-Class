def myMap(func, data):
    for v in data:
        yield func(v)
def main():
    n = int(input())
    data = list(map(int, input().split()))

main()