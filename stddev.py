def main():
    n = int(input())
    data = []
    read = 1
    total = 0
    while read <= n:
        data.append(float(input()))
        total = total + data[read-1]
        read = read + 1
    # ->total = sum(data)
    avg = total / n # =avg(data)
    print('avg:',avg)
    # cal stddev
    total = 0
    index = 0
    while index < n:
        total = total + (data[index]-avg)**2
        index = index + 1
    stddev = (total/n)**0.5
    print('stddev:',stddev)

if __name__ == '__main__':
    main()
