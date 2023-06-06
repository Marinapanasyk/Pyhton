def writing_scv():
    surname = input('Введите фамилию: ')
    if not surname.isalpha():
        print("Ошибка! Фамилию вводить буквами")
        return
    name = input('Введите имя: ')
    if not name.isalpha():
        print("Ошибка! Фамилию вводить буквами")
        return
    patronymic = input('Введите отчество: ')
    if not patronymic.isalpha():
        print("Ошибка! Фамилию вводить буквами")
        return
    phone_number = input('Введите номер телефона: ')
    if len(phone_number) != 11:
        print('В номере телефона должно быть 11 цифр.')
    else:
        phone_number = int(phone_number)
    description = input('Введите описание: ')
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as my_f:
        my_f.write(f"{surname}         {name}             {patronymic}       {phone_number }     {description}\n")

def read_date():
    file = 'Phonebook.csv'
    with open(file, 'r', encoding='utf-8') as my_f:
        print(my_f.read())



def find_date():
    sn = input("Ввeдите фамилию , которую нужно найти :  ")
    file = 'Phonebook.csv'
    with open(file, 'r', encoding='utf-8') as my_f:
        for line in my_f.readlines():
            if line.startswith(sn):
                print(line)

def del_date():
    sn = input("Ввeдите фамилию , которую нужно удалить :  ")
    file = 'Phonebook.csv'
    with open(file, 'r+', encoding='utf-8') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if sn not in line:
                f.write(line)
        f.truncate()