def own_max(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max

print("The highest number is: ", own_max([int(input("Enter a number: ")) for x in range(5)]))
