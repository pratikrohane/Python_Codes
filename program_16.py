# Find all duplicate character in string

from collections import Counter

string = 'python_programming'

elements_dict = Counter(string)

index = 0
for i in elements_dict.values():
    if(i > 1):
        print(elements_dict.keys()[index])

    index += 1