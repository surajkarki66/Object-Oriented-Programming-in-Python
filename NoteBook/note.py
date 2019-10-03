import datetime

last_id = 0
class Note:
    """ Represent note in notebook"""

    def __init__(self,memo,tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        self.id = last_id


    def match(self,filter):
        return filter in self.memo or filter in self.tags



class NoteBook:
    """ it represents the collections of notes"""
    
    def __init__(self):
        self.notes = []

    def new_note(self,memo,tags=''):
        self.notes.append(Note(memo,tags))

    def modify_memo(self,note_id,memo):
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break


    def modify_tags(self,note_id,tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break


    def search(self,filter):
        return [note for note in self.notes if note.match(filter)]

    