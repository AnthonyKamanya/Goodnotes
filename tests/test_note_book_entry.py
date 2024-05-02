from lib.note_book_entry import DiaryEntry

"""
Given a title and content
#count_words should return the number of words 
in the content
"""

def test_the_num_of_words_in_content():
    note_entry = DiaryEntry("first_business","Airbnb_property")
    result = note_entry.count_words()
    assert result == 1

"""
Given 2 words as entry and 2 wpm 
#reading_time will return 1 minute
"""

def test_2_words_with_2_wpm_should_return_1():
    note_entry = DiaryEntry("first_business","Airbnb_property Youtube")
    note_entry.count_words()
    result = note_entry.reading_time(2)
    assert result == 1

"""
Given 2 words as entry and 2 wpm 
#reading_time will return 1 minute
"""

def test_1_words_with_2_wpm_should_return_1():
    note_entry = DiaryEntry("first_business","Youtube")
    note_entry.count_words()
    result = note_entry.reading_time(2)
    assert result == 1