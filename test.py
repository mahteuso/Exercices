
def fat(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fat(x - 1)
if __name__ == '__main__':
    print(fat(100))


