n = int(input('De qual número você deseja saber a tabuada? '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
