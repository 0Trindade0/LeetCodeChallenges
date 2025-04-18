"""For two strings s and t, we say "t divides s" if and only if:
s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 """

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
