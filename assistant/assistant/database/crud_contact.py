from mongoengine import Q
from pymongo.errors import DuplicateKeyError

import assistant.assistant.database.connect
from assistant.assistant.database.models import Contact


def exist_contact(full_name):
    return Contact.objects(full_name=full_name).count()


def get_count():
    return Contact.objects.count()


def get_contact_by_num(num=0):
    return Contact.objects[num]


def get_contact_by_name(full_name):
    contact = Contact.objects(full_name=full_name).get()
    return contact


def get_contact_by_id(id_):
    return Contact.objects(id=id_).get()


def create_contact(full_name, email=None, address=None, birthday=None, phones=None):
    contact = Contact(full_name=full_name, email=email, address=address, birthday=birthday, phones=phones).save()
    return contact


def create_phone(contact_id: str, cell_phone: str):
    Contact.objects(id=contact_id).update_one(push__phones=cell_phone)


def delete_phone(contact_id: str, cell_phone: str):
    print()
    Contact.objects(id=contact_id).update_one(pull__phones=cell_phone)

# ----------------------------------------------------------------------------------


def update_contact(id_: str, email: str = None, address: str = None, birthday=None):
    contact = Contact.objects(id=id_).get()
    if email is not None:
        Contact.objects(id=id_).update_one(email=email)
    if address is not None:
        Contact.objects(id=id_).update_one(address=address)
    if birthday is not None:
        Contact.objects(id=id_).update_one(birthday=birthday)
    return contact


def remove_contact(contact_id: int):
    Contact.objects(id=contact_id).delete()


def find_contact(find_text: str):
    return Contact.objects(full_name__icontains=find_text)


if __name__ == '__main__':
    # contacts = session.query(Contact).offset(0).limit(0).all()
    # contacts = session.query(Contact).filter(Contact.full_name == 'Misha_6').first()
    # print(contacts.id)
    # for c in contacts:
    #     print(f'{c.full_name}, {c.email}, {[t.cell_phone for t in c.phones]}')
    # print(get_contact_by_id(id_='63b72a0a65b3762751478a91'))
    con = get_contact_by_name(full_name='Натан Гертрудович Фадеев')
    print(con.id)
    print(get_contact_by_id(id_=con.id))

