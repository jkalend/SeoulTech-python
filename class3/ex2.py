d = {}
while True:
    a = input("enter a command").lower()
    match a:
        case "input":
            d[input("Enter name: ")] = input("Enter number: ")
        case "search":
            try:
                print(d[input("Enter name: ")])
            except KeyError:
                print("Key not found")
        case "delete":
            try:
                del d[input("Enter name: ")]
            except KeyError:
                print("Key not found")
        case "quit":
            print("Goodbye")
            break
