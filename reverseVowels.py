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
        
