def healthy_sleep(a, b, h):
    if a <= b:
        if h < a:
            print('Deficiency')
        elif a <= h <= b:
            print('Normal')
        elif b < h:
            print('Excess')
    else:
        print('Enter A <= B')


healthy_sleep(int(input()), int(input()), int(input()))
