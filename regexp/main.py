import re
import csv

pattern = r"(^\+?[8|7])?\s?\(?(\d{3})\)?[\s-]?(\d{3})-?(\d{2})[\s-]?(\d{2})\s?\(?(доб\.)?\s?(\d+)?\)?"
headers = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']

# Read data from file
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list_raw = list(rows)

contacts_list = []

for lastname, firstname, surname, organization, position, phone, email in contacts_list_raw[1:]:
    # Formatting phone number
    if phone:
        phone = re.sub(pattern, r"+7(\2)\3-\4-\5 \6\7", phone).strip()

    full_name_raw = " ".join([lastname, firstname, surname]).split()
    full_name_raw.append('null')

    full_name = full_name_raw[:3]

    contacts_list.append({'lastname': full_name[0],
                          'firstname': full_name[1],
                          'surname': full_name[2],
                          'organization': organization,
                          'position': position,
                          'phone': phone,
                          'email': email})

# Write data to file
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.DictWriter(f, delimiter=',', fieldnames=headers)
    datawriter.writeheader()
    datawriter.writerows(contacts_list)
