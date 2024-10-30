a = {
    (input("Enter ID: ")):
      [int(input("Enter math score: ")),
        int(input("Enter science score: ")),
        int(input("Enter history score: "))] for i in range(2)}

for key in a.keys():
    a[key] = (a[key], sum(a[key]))

m = max(a, key=lambda x: a[x][1])
print(f"Student with ID {m} has the highest total score of {a[m][1]}")
