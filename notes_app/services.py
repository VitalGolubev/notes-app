import json
import typing

from .models import Note


class NotesService:
    def __init__(self, database: str = "notes.json"):
        self.notes: typing.List[Note] = []
        self.database = database

    def load_notes(self):
        """"
        Load notes from JSON database file
        """
        with open(self.database, "r") as f:
            notes = json.load(f)
        for note in notes:
            if len(note["title"]) == 0:
                continue

            self.notes.append(Note(**note))

    def save_notes(self):
        """"
        Store notes to JSON database file
        """

    def get_by_title(self, title: str) -> typing.Optional[Note]:
        pass

    def update(self):
        pass

    def delete(self):
        pass
