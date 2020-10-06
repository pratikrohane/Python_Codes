#To check if a string is palindrome or not
string = input()

revS = string[::-1]

if (string == revS):
    print("String is Palindrome")
else:
    print("String Not Palindrome")
    