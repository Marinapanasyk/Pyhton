from Root import writing_scv, read_date, find_date,  del_date

def option():
    flag = True
    while flag:
        print("\nВас приветствует телефонный справочник!   \n Выберите пункт меню для продолжения")
        while True:
            print("1: Добавить запись в справочник")
            print("2: Поиск по фамилии")
            print("3: Удаление записи")
            print("4: Показать все контакты")
            print("5: Выход")
            ch = int(input())
            if ch not in [1, 2, 3, 4, 5]:
                print('\nВыбран неверный пункт меню, попробуйте еще раз: ')
                continue
            if ch == 1:
                writing_scv()
                break
            elif ch == 2:
                find_date()
                break
            elif ch == 3:
                del_date()
                break
            elif ch == 4:
                read_date()
            else:
                flag = False
                break
option()