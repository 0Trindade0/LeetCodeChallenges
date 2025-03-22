"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 """

s = 'IceCream'
vowels = []  
rebuild_S = [] 


for letter in s: 
    if letter in {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}:
        vowels.append(letter)

vowels = vowels[::-1]

for letter in s:
    if letter in {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}:
        rebuild_S.append(vowels.pop(0))
    else:
        rebuild_S.append(letter) 

reverse_S = ''.join(rebuild_S)
print(reverse_S)   
        
