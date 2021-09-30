documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():
    num = input('Введите номер документа: ')
    i = 0
    for document in documents:
        i += 1
        if document["number"] == num:
            return document["name"]
        elif document["number"] != num and i == len(documents):
            return 'Такого документа не существует!'


def shelf():
    num = input('Введите номер документа: ')
    i = 0
    for directory in directories:
        i += 1
        if num in directories[directory]:
            return directory
        elif i == len(directories):
            return 'Такого документа не существует!'


def list_():
    documents_list = [f'{document["type"]} "{document["number"]}" "{document["name"]}"' for document in documents]
    return documents_list


def add():
    new_dict = {
        "type": input('Введите тип документа: '),
        "number": input('Введите номер документа: '),
        "name": input('Введите имя владельца: ')
    }
    shelf_num = input('Введите номер полки: ')
    if shelf_num in list(directories):
        documents.append(new_dict)
        directories[shelf_num].append(new_dict["number"])
        return 'Новый документ добавлен!'
    else:
        return 'Такой полки не существует!'


def delete():
    num = input('Введите номер документа: ')
    for document in documents:
        if num == document["number"]:
            documents.remove(document)
            for directory in directories:
                if num in directories[directory]:
                    directories[directory].remove(num)
                    return 'Документ удален!'
        elif num != document["number"] and document == documents[-1]:
            return 'Не удалось найти документ!'


def move(num, move):
    for document in documents:
        if num == document["number"]:
            for directory in directories:
                if num in directories[directory]:
                    if move in list(directories):
                        directories[directory].remove(num)
                        directories[move].append(num)
                        return 'Документ перемещен!'
                    else:
                        return 'Такой полки не существует!'
        elif num != document["number"] and document == documents[-1]:
            return 'Такого документа не существует!'


def add_shelf():
    add_shelf = input('Введите номер полки: ')
    i = 0
    for directory in directories:
        if add_shelf != directory and i + 1 == len(directories):
            directories[add_shelf] = []
            return 'Новая полка добавлена!'
        elif add_shelf != directory:
            i += 1
        elif add_shelf == directory:
            return 'Такая полка уже существует!'


commands_dict = {'p': people, 's': shelf, 'l': list_, 'a': add, 'd': delete,
                'm': move, 'as': add_shelf}


def result():
    command = input('Введите команду: ')
    if command == 'm':
        print(commands_dict[command]("11-2", '2'))
    elif command in commands_dict.keys():
        print(commands_dict[command]())
    else:
        print('Неверная команда!')


if __name__ == '__main__':
    result()
