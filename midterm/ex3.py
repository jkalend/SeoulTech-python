try:
    words = input().replace(",", "").replace(".", "").lower().split(" ")
    print(len(set(words)))
except Exception as e:
    print("your input is invalid")
    exit(1)
