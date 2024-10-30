s = input()

a = {c: s.count(c) for c in s}
# print it as a string with the format "a3b3c2" and so on
for k, v in a.items():
    print(f"{k}{v}", end="")
