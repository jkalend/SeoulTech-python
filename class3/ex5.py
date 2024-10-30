sen = input("Enter a sentence: ").lower().replace(",", "").replace(".", "").split()
a = {i: sen.count(i) for i in set(sen)}
for key, value in a.items():
    print(f"{key}: {value}")
