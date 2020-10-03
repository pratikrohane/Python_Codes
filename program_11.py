# Python program to check if a string is palindrome or not
# when reverse of the string and original string are same then the string is Palindrome

# function which return reverse of a string 
def isPalindrome(s):
    return s == s[::-1]
 
 
s = input("Enter the String")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")