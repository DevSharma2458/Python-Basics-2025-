a = int(input("Enter a number (1-3): "))
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("a is something else")
