def status(states):
    match states:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case _:
            return "invalid"


print(status(1))
print(status(2))
print(status(3))
print(status(00))
