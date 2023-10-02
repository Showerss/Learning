def speedwagon(bar):
    found = False
    for i in range(len(bar) - 1):
        if bar[i] == bar[i+1]:
            found = True
        else:
            found = False
    return found
print(speedwagon("Hello"))