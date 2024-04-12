documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

### My
def get_name(doc_number):
    result = "Документ не найден"

    for document in documents:
        if doc_number in document["number"]:
            result = document["name"]

    return result


def get_directory(doc_number):
    result = "Полки с таким документом не найдено"

    for number in directories:
        if doc_number in directories[number]:
            result = number

    return result


def add(document_type, number, name, shelf_number):
    new_document = {"type": document_type, "number": number, "name": name}
    documents.append(new_document)

    if shelf_number in directories:
        if number not in directories[str(shelf_number)]:
            directories[str(shelf_number)].append(str(number))
    else:
        directories[str(shelf_number)] = [str(number)]

### Netology
def get_name(doc_number):
    for document in documents:
        if document['number'] == doc_number:
            return document['name']
    return "Документ не найден"


def get_directory(doc_number):
    for number, docs in directories.items():
        if doc_number in docs:
            return number
    return "Полки с таким документом не найдено"


def add(document_type, number, name, shelf_number):
    new_doc = {"type": document_type, "number": number, "name": name}
    documents.append(new_doc)
    if shelf_number in directories:
        directories[shelf_number].append(number)
    else:
        directories[shelf_number] = [number]


if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))
