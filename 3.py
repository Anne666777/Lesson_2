my_list = ['winter', 'spring', 'summer', 'autumn']
my_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Enter month: "))
if month == 1 or month == 12 or month == 2:
    print(my_list[0] + ' - list')
    print(my_dict.get(1) + ' - dict')
elif month == 3 or month == 4 or month == 5:
    print(my_list[1] + ' - list')
    print(my_dict.get(2) + ' - dict')
elif month == 6 or month == 7 or month == 8:
    print(my_list[2] + ' - list')
    print(my_dict.get(3) + ' - dict')
elif month == 9 or month == 10 or month == 11:
    print(my_list[3] + ' - list')
    print(my_dict.get(4) + ' - dict')
else:
    print("Sorry, but you entered the wrong month value. Try again")
