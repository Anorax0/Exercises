# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


def zip_generator(start: str, stop: str):
    start_num = start.split('-')
    start1, start2 = int(start_num[0]), int(start_num[1])

    zip_list = [start]

    while True:
        if str(start1)+"-"+str(start2) == stop:
            return zip_list
        if start2 > 998:
            start2 = 0
            start1 += 1
        start2 += 1
        if len(str(start2)) == 1:
            zip_list.append(str(start1)+"-00"+str(start2))
        elif len(str(start2)) == 2:
            zip_list.append(str(start1) + "-0" + str(start2))
        else:
            zip_list.append(str(start1)+"-"+str(start2))


test = zip_generator("79-900", "80-155")
print(test)
