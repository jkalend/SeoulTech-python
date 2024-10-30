a = {input("Enter name: "): input("Enter number: ") for i in range(5)}

print(a.keys())
try:
    print(a[(input("Enter key: "))])
except KeyError:
    print("Key not found")
