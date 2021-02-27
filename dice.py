import random as ran

key = input("Press y to start ")
print("This is a test")
while key == 'y':
    num = ran.randint(1, 6)
    if num == 1:
        for i in range(5):
            if i == 0:
                print('[', end=(11 * '-') + ']')
                print()
            elif i == 4:
                print('[', end=(11 * '-') + ']')
            elif i == 2:
                print(f'[     {0}     ]', end="\n")
            else:
                print(f'[           ]', end="\n")

        print()
        key = input("Press y to start ")
    elif num == 2:
        for i in range(5):
            if i == 0:
                print('[', end=(11 * '-') + ']')
                print()
            elif i == 4:
                print('[', end=(11 * '-') + ']')
            elif i == 2:
                print(f'[   {0}   {0}   ]', end="\n")
            else:
                print(f'[           ]', end="\n")

        print()
        key = input("Press y to start ")

    elif num == 3:
        for i in range(5):
            if i == 0:
                print('[', end=(11 * '-') + ']')
                print()
            elif i == 4:
                print('[', end=(11 * '-') + ']')
            else:
                print(f'[     {0}     ]', end="\n")

        print()
        key = input("Press y to start ")

    elif num == 4:
        for i in range(5):
            if i == 0:
                print('[', end=(11 * '-') + ']')
                print()
            elif i == 4:
                print('[', end=(11 * '-') + ']')
            elif i == 1:
                print(f'[   {0}   {0}   ]', end="\n")
            elif i == 3:
                print(f'[   {0}   {0}   ]', end="\n")
            else:
                print(f'[           ]', end="\n")

        print()
        key = input("Press y to start ")
    elif num == 5:
        for i in range(5):
            if i == 0:
                print('[', end=(11 * '-') + ']')
                print()
            elif i == 4:
                print('[', end=(11 * '-') + ']')
            elif i == 1:
                print(f'[   {0}   {0}   ]', end="\n")
            elif i == 3:
                print(f'[   {0}   {0}   ]', end="\n")
            else:
                print(f'[     {0}     ]', end="\n")

        print()
        key = input("Press y to start ")

    elif num == 6:
        for i in range(5):
            if i == 0:
                print('[', end=(11 * '-') + ']')
                print()
            elif i == 4:
                print('[', end=(11 * '-') + ']')
            elif i == 1:
                print(f'[   {0}   {0}   ]', end="\n")
            elif i == 3:
                print(f'[   {0}   {0}   ]', end="\n")
            else:
                print(f'[   {0}   {0}   ]', end="\n")

        print()
        key = input("Press y to start ")
