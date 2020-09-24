def square_sum(num):
    s_sum = 0
    for i in range(1, num+1):
        s_sum += i**2

    return s_sum

num = int(input())
print(square_sum(num))
