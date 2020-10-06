#To check if small string is there in big string

string = input()
sub_str = input()

if(string.find(sub_str) == -1):
    print("No")
else:
    print("Yes")