def power(base,multiplier):
    if multiplier == 1:
        return base
    else:
        return base * power(base,multiplier-1)
print(power(10,5))
