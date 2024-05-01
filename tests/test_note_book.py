from lib.note_book import Diary
"""
Initially there are 
no notes entry
"""
def test_initially_no_notes_entry():
    note_book = Diary()
    results= note_book.all() 
    assert results == []