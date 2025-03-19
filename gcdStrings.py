import math

str1 = input('STR1: ')
str2 = input('STR2: ')
str_cut = ''

gcd = math.gcd(len(str1), len(str2))

if gcd <= 0:
     print(str_cut)
elif gcd >= 1:
    for letter in str2:
        str_cut += letter 

print(str_cut)
