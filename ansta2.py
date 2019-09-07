#  ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
#  NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

from itertools import chain


def check_missings(*args: list, target: int):
    missings = []
    unpacked = sorted(chain(*args))
    for i in range(1, target+1):
        if i not in unpacked:
            missings.append(i)
    return unpacked, missings, target


test = check_missings([2, 3, 7, 4, 9], target=10)
print(f'Input: {test[0]}, {test[2]}')
print(f'Output: {test[1]}')
