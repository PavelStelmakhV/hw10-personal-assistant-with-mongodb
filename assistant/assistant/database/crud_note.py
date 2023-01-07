from mongoengine import Q
from pymongo.errors import DuplicateKeyError

from assistant.assistant.database.models import Note, Tag
import assistant.assistant.database.connect


def get_count():
    return Note.objects.count()


def exist_note(title: str) -> bool:
    return Note.objects(title=title).count()


def exist_tag(name: str) -> bool:
    return Tag.objects(name=name).count()


def get_note_by_name(title):
    note = Note.objects(title=title)
    return note[0]


def create_note(title, description=None, tags_name_list=None):
    tags_list = []
    for tag_name in tags_name_list:
        tag = _add_tag(tag_name)
        tags_list.append(tag)
    note = Note(title=title, description=description, tags=tags_list).save()
    return note


def update_note(title, description=None, add_text=False):
    note = get_note_by_name(title=title)
    if add_text:
        description = note.description + '\n' + description
    note.update(description=description)
    return note


def remove_note(title):
    note = get_note_by_name(title=title)
    note.delete()


def _add_tag(tag_name: str) -> Tag:
    if exist_tag(name=tag_name):
        tag = Tag.objects(name=tag_name).get()
    else:
        tag = Tag(name=tag_name).save()
    return tag


def _del_tag(tag: Tag):
    if not Note.objects(tags=tag).count():
        tag.delete()


def create_tag(note_title: str, tag_name: str):
    tag = _add_tag(tag_name)
    Note.objects(title=note_title).update_one(push__tags=tag)


def remove_tag(note_title: str, tag_name: str) -> bool:
    if not exist_tag(name=tag_name):
        return False
    tag = Tag.objects(name=tag_name).get()
    Note.objects(title=note_title).update_one(pull__tags=tag)
    _del_tag(tag=tag)
    return True


def find_note(find_text: str):
    notes = Note.objects(Q(title__icontains=find_text) | Q(description__icontains=find_text))
    return notes


def notes_all():
    return Note.objects()


def tags_all():
    return Tag.objects()


def find_note_by_tag(tag_name: str):
    if len(tag_name) > 0:
        tag = Tag.objects(name=tag_name).get()
        return Note.objects(tags=tag)
    else:
        notes = Note.objects(tags=[])
        return notes


if __name__ == '__main__':
    pass

