from faker import Faker
import random

from assistant.assistant.database import crud_note


fake = Faker('ru-RU')
count_notes = 10
notes = ['note_1', 'note_2', 'note_3', 'note_4', 'note_5', 'note_6', 'note_7']


def create_note():

    for _ in range(count_notes):
        crud_note.create_note(
            title=fake.sentence(nb_words=2),
            description=fake.paragraph(nb_sentences=3, variable_nb_sentences=False),
            tags_name_list=[random.choice(notes), ]
        )


if __name__ == '__main__':
    create_note()

