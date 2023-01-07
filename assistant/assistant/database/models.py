from mongoengine import Document
from mongoengine.fields import DateTimeField, ListField, StringField, ReferenceField

from assistant.assistant.database.connect import connect


class Contact(Document):
    full_name = StringField(required=True, unique=True)
    email = StringField(unique=True)
    address = StringField(max_length=250)
    birthday = DateTimeField()
    phones = ListField(StringField(max_length=25))


class Tag(Document):
    name = StringField(max_length=250, nullable=False, unique=True)


class Note(Document):
    title = StringField(max_length=250, nullable=False, unique=True)
    description = StringField()
    tags = ListField(ReferenceField(Tag))



