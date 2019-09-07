#  ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

# Nie byłem pewien czy chodzi o liczby typu decimal czy o zwykłe liczby dziesiętne (float), stąd dwie wersje

from decimal import *


def gen_decimal_range(start, stop, step):
    steps = (stop - start) / step
    result = [Decimal(start)]
    while steps != 0:
        start += step
        result.append(Decimal.from_float(start))
        steps -= 1
    return result


def gen_range(start, stop, step):
    steps = (stop - start) / step
    result = [float(start)]
    while steps != 0:
        start += step
        result.append(start)
        steps -= 1
    return result


test = gen_decimal_range(2, 5.5, 0.5)
print(test)

test = gen_range(2, 5.5, 0.5)
print(test)
