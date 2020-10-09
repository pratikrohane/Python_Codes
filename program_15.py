#Largest element in an Array 

arr = list(map(int, input().split()))
LE = arr[0]

for i in arr[1:]:
    if(LE < i):
        LE = i 

print(LE)