#Permutations of a String
from itertools import permutations 

string = input()
#Get all possible tuples of permutations
per_list = permutations(string)

for i in list(per_list):
    print(''.join(i))