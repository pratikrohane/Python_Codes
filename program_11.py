#Even from List

lt = list(map(int, input().split()))

for i in lt:
    if i % 2 == 0 and i > 0:
        print(i)