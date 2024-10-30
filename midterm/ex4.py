from random import randint

rolls = 1000
probs = 0
for i in range(rolls):
    dies = [randint(1,6) for i in range(10)]
    for j in dies:
        if dies.count(j) == 5:
            probs += 1

print(probs / rolls)
