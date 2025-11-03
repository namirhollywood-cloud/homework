# Данные
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_owner_by_number(documents, number):
    for document in documents:
        if document['number'] == number:
            return document['name']
    return None



def main():
    while True:
        command = input("Введите команду (r - узнать владельца, q - выйти): ").strip().lower()

        if command == 'q':
            print("Программа завершена.")
            break

        elif command == 'r':
            doc_number = input("Введите номер документа: ").strip()
            owner = get_owner_by_number(documents, doc_number)

            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Документ не найден.")
        else:
            print("Неизвестная команда. Попробуйте снова.")


v
if __name__ == "__main__":
    main()