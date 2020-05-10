
def quickPow(base, power):
    if power == 0:
        return 1
    result = 1
    basecopy = base
    while power > 0:
        if power % 2 == 1:
            result = result * basecopy
        basecopy = basecopy*basecopy
        power = power / 2
    return result




out = quickPow(2, 33)
print(out)
