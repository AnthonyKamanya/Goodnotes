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

"""
Given I add two notes
I can count the number of words in my notes
"""

def test_count_words_in_notes():
    note_book = Diary()
    note_book_entry_first = DiaryEntry("first_business","Airbnb_property")
    note_book_entry_second = DiaryEntry("Second_business","Youtube_property")
    note_book.add(note_book_entry_first)
    note_book.add(note_book_entry_second)
    result = note_book.count_words()
    assert result == 2

"""
Given 2 words with 2wpm
#reading_time will return 1
"""

def test_estimated_time_to_read_notes():
    note_book = Diary()
    note_book_entry_first = DiaryEntry("first_business","Airbnb_property")
    note_book_entry_second = DiaryEntry("Second_business","Youtube_property")
    note_book.add(note_book_entry_first)
    note_book.add(note_book_entry_second)
    result = note_book.reading_time(2)
    assert result == 1

"""
Given 5 words with 2wpm
#reading_time will return 1
"""

def test_estimated_time_to_read_notes_with_5_words():
    note_book = Diary()
    note_book_entry_first = DiaryEntry("first_business","Airbnb Property")
    note_book_entry_second = DiaryEntry("Second_business","Youtube rental")
    note_book_entry_third = DiaryEntry("third_business","AmazonFBA")
    note_book.add(note_book_entry_first)
    note_book.add(note_book_entry_second)
    note_book.add(note_book_entry_third)
    result = note_book.reading_time(2)
    assert result == 3