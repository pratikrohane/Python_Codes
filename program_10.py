#Sum of elements in Array 

arr = list(map(int, input().split()))

sum = 0

for i in arr:
    sum += i
    
print(sum)