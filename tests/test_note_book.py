import pytest
from lib.note_book import Diary
"""
Initially there are 
no notes entry
"""
def test_initially_no_notes_entry():
    note_book = Diary()
    results= note_book.all() 
    assert results == []


"""
Initially if there are 
#reading_time will raise an exception error
"""
def test_initially_no_notes_entry_raises_err():
    note_book = Diary()
    with pytest.raises(Exception) as err:
        note_book.reading_time(2)
    error_message = str(err.value)
    assert error_message == "Cannot Estimate reading time for no entry or 0 wpm"


"""
if there are wpm is 0
#reading_time will raise an exception error
"""
def test_wpm_is_0():
    note_book = Diary()
    with pytest.raises(Exception) as err:
        note_book.reading_time(0)
    error_message = str(err.value)
    assert error_message == "Cannot Estimate reading time for no entry or 0 wpm"