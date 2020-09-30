#Check Year leaf Year or Not

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leaf Year")
        else:
            print("Not Leaf Year")
    else:
        print("Leaf Year")
else:
    print("Not Leaf Year")