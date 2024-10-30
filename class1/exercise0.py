s1 = input("Enter a string: ")
s2 = input("Enter a substring to find: ")

[print(f"Found at index {a}") for a in range(len(s1)) if s1[a:].startswith(s2)]

# i = 0
# while (a := s1.find(s2, i)) != -1:
#     print(f"Found at index {a}")
#     i = a + 1

# if i == 0:
#     print(-1)
