def open_file():
    with open('phonebook.txt', 'r') as file:
        return file.read()
def print_data():
    print(read_file())
    
def interface():
    command = ''
    while command != '4':
        command = input("Введите команду: ")
        match command:
            case '1':
                input_data()
            case '2':
                print_data()
            case '3':
                search_contact()
            case '4':
                print("До свидания")
            case _:
                print(command)
                print('Некорректный ввод.')

interface()