def average(*args):
    num = 0.0
    if args:
        return sum(args) / len(args)
    else:
        return 0.0
print (average())
print (average(1, 2))
print (average(1, 2, 2, 3, 4))