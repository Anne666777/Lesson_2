my_list = [7, 5, 3, 3, 2]
while True:
    value = input('Enter a number: ')
    if not value.isdigit(): # Возвращает флаг, указывающий на то, содержит ли строка только цифры. Вернёт True,
        # если в строке хотя бы один символ и все символы строки являются цифрами, иначе — False
        print("ERROR, try again!")
        continue
    else:
        value = int(value)
    idx = None
    for i, num in enumerate(my_list):
        if value > num:
            idx = i
            break
    if idx is None:
        my_list.append(value)
    else:
        my_list.insert(idx, value)
    print(my_list)



