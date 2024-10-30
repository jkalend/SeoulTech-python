numbers = [int(input()) for i in range(3)]
numbers.sort()

i = 1
while True:
    LCM = numbers[0] * i
    i += 1
    if LCM % numbers[1] == 0 and LCM % numbers[2] == 0:
        print(LCM)
        break
