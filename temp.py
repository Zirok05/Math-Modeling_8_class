
def makaka_function (x):
    if (x % 4 == 0 or x % 100 != 0 and x % 400 == 0):
        print('высокосный')
    else:
        print('Обычный')
makaka_function(2020)