# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в
# текстовом файле
# Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# Использование функций. Ваша программа
# не должна быть линейной

import os
import time

ENC = 'UTF-8'
PATH = "phonebook.txt"
PATH_FAVORITE = "favorite_contacts.txt"

def interface():
    while True:
        print("Меню:\n"
            "1: Добавить контакт\n"
            "2: Показать все контакты\n"
            "3: Найти контакт\n"
            "4: Изменить(удалить) контакт\n"
            "5: Показать избранные"
            "6: Добавить контакт в избранные\n"
            "7: Выход")
        command = input("=> ")
        match command:
            case '1':
                add_contact()
            case '2':
                show_all()
            case '3':
                find_contact()
            case '4':
                change_contact()  # Тут надо бы добавить параллельное изменение и в списке избранных, но мне лень
            case '5':
                show_favorite()
            case '6':
                add_favorite()
            case '7':
                print("Сохранение...")
                time.sleep(3)
                print("Готово.")
                return
            case _:
                print("Ошибка ввода.\nПовторите попытку\n\n")

def add_contact():
    with open(PATH, 'r+', encoding=ENC) as f:
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        number = input("Введите номер телефона: ")
        address = input("Введите адрес: ")
        new_contact = f"{surname} {name} {number} {address}\n"
        contact_list = f.readlines()
        for contact in contact_list:
            if number not in contact.split():
                f.write(f"{new_contact}")
        else:
            print("Контакт с указанным номером уже существует\n")

def show_all():
    with open(PATH, 'r', encoding=ENC) as f:
        print(f.read())

def find_contact(param = None):
    with open(PATH, 'r', encoding=ENC) as f:
        if param != '3':
            print("По какому параметру производить поиск:\n"
                "1) Фамилия\n"
                "2) Имя\n"
                "3) Номер телефона\n"
                "4) Адрес")
            param = input("=> ")
            if param not in '1,2,3,4':
                return print('Ошибка ввода')
            desired_param = input("Введите значение искомого параметра: ")
        else:
            desired_param = input("Введите номер телефона: ")
        contact_list = f.readlines()
        for current_contact in contact_list:
            current_contact_lst = current_contact.replace("\n", "").split()
            if desired_param in current_contact_lst[int(param) - 1]:
                print(current_contact)
                if param == '3':
                    return current_contact

def change_contact():
    original_value = find_contact('3')
    original_lst = original_value.split()
    print("Выберите изменяемый параметр:\n"
          "1) Фамилия\n"
          "2) Имя\n"
          "3) Номер телефона\n"
          "4) Адрес\n"
          "5) Удалить контакт")
    param = input("=> ")
    if param not in '1,2,3,4,5':
        return print("Некорректный ввод")
    if param != '5':
        new_value = input("Введите новое значение: ")
        original_lst[int(param) - 1] = new_value
        new_value_str = ' '.join(original_lst) + '\n'
    else:
        new_value_str = ''
    
    NEW_PATH = PATH[:-4] + '_edited' + PATH[-4:]
    with open(PATH, 'r', encoding=ENC) as orig, open (NEW_PATH, 'w', encoding=ENC) as edited:
        orig_file = orig.readlines()
        for line in orig_file:
            if line != original_value:
                edited.write(line)
            else:
                edited.write(new_value_str)
    
    os.remove(PATH)
    os.rename(NEW_PATH, PATH)

def add_favorite():
    desired_contact = find_contact('3')
    accept = input('Желаете добавить этот контакт в избранные? (Y/N): ')
    match accept.upper():
        case 'Y':
            desired_contact.replace('\n', '')
            with open(PATH_FAVORITE, 'r', encoding=ENC) as f:
                if desired_contact in f.read():
                    return print("Контакт уже в избранном.")
            with open(PATH_FAVORITE, 'a', encoding=ENC) as f:
                f.write(desired_contact)
        case 'N':
            return
        case _:
            return print('Некорректный ввод')

def show_favorite():
    with open(PATH_FAVORITE, 'r', encoding=ENC) as f:
        print(f.read())

interface()