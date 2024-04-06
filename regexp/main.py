import re
import csv

PATTERN = r"(^\+?[8|7])?\s?\(?(\d{3})\)?[\s-]?(\d{3})-?(\d{2})[\s-]?(\d{2})\s?\(?(доб\.)?\s?(\d+)?\)?"
HEADERS = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']


def read_data():
    # Read data from file
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        response = list(rows)

    return response


def write_data(data):
    # Write data to file
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.DictWriter(f, delimiter=',', fieldnames=HEADERS)
        datawriter.writeheader()
        datawriter.writerows(data)


def formatting_data(data):
    response = []

    for lastname, firstname, surname, organization, position, phone, email in data[1:]:
        fio = {}

        fio_key, fi_key = "", ""
        # Formatting phone number
        if phone:
            phone = re.sub(PATTERN, r"+7(\2)\3-\4-\5 \6\7", phone).strip()

        full_name = " ".join([lastname, firstname, surname]).split()

        if len(full_name) == 3:
            fio.update({'lastname': full_name[0], 'firstname': full_name[1], 'surname': full_name[2]})
            fio_key = "".join(fio.values())
            fi_key = "".join(dict(list(fio.items())[:2]).values())
        elif len(full_name) == 2:
            fio.update({'lastname': full_name[0], 'firstname': full_name[1], 'surname': ''})
            fi_key = "".join(fio.values())

        response.append({
            'fio_key': fio_key,
            'fi_key': fi_key,
            'data': {**fio, 'organization': organization, 'position': position, 'phone': phone, 'email': email}
        })

    return response


def data_normalization(data):
    response = []
    delete_index = []

    for id1, i in enumerate(data[:-1]):
        key1 = i['fio_key']
        key2 = i['fi_key']
        print(f"\nCheck keys: {key1}, {key2}")

        if id1 in delete_index:
            continue
        else:
            id2 = id1 + 1
            for j in data[id2:]:
                key_pair = [j["fio_key"], j["fi_key"]]

                if key1 not in key_pair and key2 not in key_pair:
                    pass
                else:
                    delete_index.append(id2)

                    if data[id1]["data"]["organization"] == data[id2]["data"]["organization"]:
                        new_organization = data[id1]["data"]["organization"]
                    else:
                        new_organization = data[id1]["data"]["organization"] + data[id2]["data"][
                            "organization"]

                    data[id1]["data"].update({
                        'organization': new_organization,
                        'position': data[id1]["data"]["position"] + data[id2]["data"]["position"],
                        'phone': data[id1]["data"]["phone"] + data[id2]["data"]["phone"],
                        'email': data[id1]["data"]["email"] + data[id2]["data"]["email"]
                    })

                    if key1 in key_pair:
                        print(f"Merge {id1} and {id2}, delete {id2}...")
                        print(f"Key pair: {key_pair}")
                    elif key2 in key_pair:
                        print(f"Merge {id1} and {id2}, update key1 <=> key2, delete {id2}...")
                        print(f"Key pair: {key_pair}")

                        if data[id1]["fio_key"]:
                            new_key = data[id1]["fio_key"]
                        else:
                            new_key = data[id2]["fio_key"]

                        data[id1].update({"fio_key": new_key})
                id2 += 1

    for id, item in enumerate(data):
        if id not in delete_index:
            response.append(data[id]["data"])

    return response


def main():
    # Read data
    contacts_list_raw = read_data()
    # Add keys, formatting data
    contacts_list = formatting_data(contacts_list_raw)
    # Merge data, delete duplicates
    contact_list_final = data_normalization(contacts_list)
    # Write data
    write_data(contact_list_final)


if __name__ == '__main__':
    main()
