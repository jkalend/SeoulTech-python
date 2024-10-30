a = {
    (input("Enter ID: ")):
      [int(input("Enter math score: ")),
        int(input("Enter science score: ")),
        int(input("Enter history score: "))] for i in range(2)}

for key in a.keys():
    a[key] = (a[key], sum(a[key]))

for key, value in a.items():
    print(f"ID: {key}, Total: {value[1]}") if value[1] >= 100 else None
