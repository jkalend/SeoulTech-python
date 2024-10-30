def is_prime(i):
    if i < 2:
        return False
    for x in range(2, i):
        if i % x == 0:
            return False
    return True

print([x for x in range(int(input("Enter a number: "))) if is_prime(x)])
