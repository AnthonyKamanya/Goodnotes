from lib.note_book import Diary
from lib.note_book_entry import DiaryEntry
"""
Given I add two notes
I can see them represented in a list
"""
def test_add_multiple_notes_and_list_them():
    note_book = Diary()
    note_book_entry_first = DiaryEntry("first_business","Airbnb_property")
    note_book_entry_second = DiaryEntry("Second_business","Youtube_property")
    note_book.add(note_book_entry_first)
    note_book.add(note_book_entry_second)
    result = note_book.all()
    assert result == [note_book_entry_first,note_book_entry_second]


