a = [int(input("Enter a number: ")) for x in range(5)]
print(a.sort(reverse=True))

def own_reverse(list):
    return list[::-1]
