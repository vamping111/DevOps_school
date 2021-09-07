def recur(string):
    if (len(string) == 1):
        return ord(string[0]) - ord('0')
    first = recur(string[1:])
    nexxt = ord(string[0]) - ord('0')
    nexxt = nexxt * (10 ** (len(string) - 1)) + first
    return int(nexxt)

while True:
    value = input("Enter your value: ")
    result = recur(value)
    if value == 'cancel':
        print("Bye!")
        exit()
    elif result%2 == 0:
        print((int(result)) / 2)
    else:
        print((int(result))*3+1)
