def is_year_leap(year):
    if year % 400 == 0:
        print('Leap')
    elif year % 4 == 0 and not year % 100 == 0:
        print('Leap')
    else:
        print('Ordinary')


is_year_leap(int(input()))
