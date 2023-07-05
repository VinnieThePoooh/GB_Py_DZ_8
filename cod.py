# def readfile(file):
#     data = [i.split() for i in open(file, 'r', encoding='utf-8')]
#     return data


def print_info(file):
    with open(file , 'r', encoding='utf-8') as f:
        print(f.read())


def write_info(file):
    name = input('Введите имя контакта: ')
    number = input('Введите номер контакта: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(name + ' - ' + number + '\n')
    print('Готово')

def change_info(file):
    with open(file, 'r', encoding='utf-8') as f:
        counter = 1
        for i in f:
            print(str(counter) + ')'+' ' +i)
            counter+=1
    user_choice=int(input('Выберите номер контакта, в котором хотите внести изменения: '))
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines.pop(user_choice-1)
    print(lines)
    with open(file, 'w', encoding='utf-8') as f:
        for i in range (0, len(lines)):
            f.write(lines[i])
    name = input('Введите имя контакта: ')
    number = input('Введите номер контакта: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(name + ' - ' + number + '\n')
    print('Готово')
       
def good_bye():

    print('До свидания')


def main():
    user_choice = -1
    while user_choice !=0:
        # data = readfile('phone_numbers.txt')
        # print(data)
        print('Чтобы закрыть книгу контактов, нажмите 0')
        print('Чтобы посмотреть книгу контактов, нажмите 1')
        print('Чтобы записать новый контакт, нажмите 2')
        print('Чтобы изменить существующий контакт, нажмите 3')
        user_choice = int(input())
        operation = {0: good_bye, 1: print_info, 2: write_info, 3: change_info }
        if user_choice == 0:
            operation[user_choice]()
        else:
            operation[user_choice]('phone_numbers.txt')


main()
