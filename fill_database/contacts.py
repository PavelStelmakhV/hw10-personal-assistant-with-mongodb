from faker import Faker

from assistant.assistant.database import crud_contact


fake = Faker('ru-RU')
count_contact = 10


def create_contacts():
    for _ in range(count_contact):
        crud_contact.create_contact(
            full_name=fake.name(),
            email=fake.email(),
            address=fake.street_address(),
            birthday=fake.date_between(start_date="-50y", end_date='-15y'),
            phones=[fake.phone_number(), fake.phone_number()]
        )


#
# def fill_date():
#     contacts = session.query(Contact).all()
#     for contact in contacts:
#         contact.birthday = fake.date_between(start_date="-50y", end_date='-15y')
#         session.add(contact)
#     session.commit()
#
#
# def create_phones():
#     contacts = session.query(Contact).all()
#     for _ in range(count_contact):
#         phone = Phone(
#             cell_phone=fake.phone_number(),
#             contact_id=random.choice(contacts).id
#         )
#         session.add(phone)
#     session.commit()


if __name__ == '__main__':
    create_contacts()
    # fill_date()
    # create_phones()

