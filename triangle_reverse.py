def print_star(level):
    for upper_level in range(1, level + 1):
        for i in range(0, level - upper_level):
            print(" ", end="")
        for i in range(0, (upper_level - 1) * 2 + 1):
            print("*", end="")
        for i in range(0, level - upper_level):
            print(" ", end="")
        print('\n')
    for lower_level in range(level + 1, 2 * level):
        for i in range(0, level - (2 * level - lower_level)):
            print(" ", end="")
        for i in range(0, (2 * level - lower_level - 1) * 2 + 1):
            print("*", end="")
        for i in range(0, level - (2 * level - lower_level)):
            print(" ", end="")
        print('\n')


if __name__ == '__main__':
    print_star(4)
