import os
import math


def create_contact_list(vcf_file):
    contacts = []
    contact = ""

    for line in vcf_file:
        line = line.strip()

        if not line:
            continue

        if line.startswith("BEGIN:VCARD"):
            if contact:
                contacts.append(contact)
            contact = line + "\n"
        else:
            contact += line + "\n"

    if contact:
        contacts.append(contact)
    return contacts


def group_contacts(contacts, totalContacts):
    group_len = math.floor(totalContacts / 3)
    group_list = []

    for i in range(0, len(contacts), group_len):
        group = contacts[i:i+group_len]
        group_list.append(group)
    return group_list


def save_vcf_entry(group_list, folder="out"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, group in enumerate(group_list):
        filepath = os.path.join(folder, f"booking{i+1}.vcf")
        with open(filepath, 'w') as vcf_file:
            for contact in group:
                vcf_file.write(contact)


with open('data.vcf', 'r') as vcf_file:
    contacts = create_contact_list(vcf_file)
    groups = group_contacts(contacts, len(contacts))
    save_vcf_entry(groups, "contacts")
    print(len(groups))
