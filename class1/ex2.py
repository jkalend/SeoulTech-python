vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s = input("Enter a string: ")
print(len([c for c in s if c in vowels]))
