import sys
from note import Note,NoteBook


class Menu:
    def __init__(self):
        self.note = NoteBook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }


    def display(self):
        print("""
        Menu  
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        while True:
            self.display()
            choice = input('Enter your choice:')
            action = self.choices.get(choice)

            if action:
                action()

            else:
                print("Not a valid choice")



    def show_notes(self,notes=None):
        if not notes:
            notes = self.note.notes


            for note in notes:
                print("ID=",note.id)
                print("TAGS=",note.tags)
                print("MEMO=",note.memo)
                print("DATE: ",note.creation_date)



    def search_notes(self):
        filter = input("Search for..")
        notes = self.note.search(filter)
        self.show_notes(notes)


    def add_note(self):
        memo = input("Enter the memo:")
        tags = input("Enter the tags:")
        self.note.new_note(memo,tags)
        print("Your note is created...")

    def modify_note(self):
        id = input("Enter the id of the note:")
        memo = input("Enter the memo:")
        tags = input("Enter the tags:")
        if memo:
            self.note.modify_memo(id,memo)
        if tags:
            self.note.modify_tags(id,tags)

    def quit(self):
        print("Thank you")
        sys.exit(0)



if __name__ == "__main__":
    Menu().run()