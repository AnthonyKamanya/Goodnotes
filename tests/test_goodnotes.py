from lib.goodnotes import *
import pytest

"""
Given a title and an empty content
raises an error messsage which takes care of emtpy title and contents
"""
def test_errors_with_empty_title():
    goodnotes= Goodnotes
    with pytest.raises(Exception) as err:
        goodnotes("title","")
    error_message = str(err.value)
    assert error_message == "Goodnotes entries must have title and contents"

"""
Given content and an empty title
raises an error messsage which takes care of emtpy title and contents
"""
def test_errors_with_empty_content(): 
    goodnotes= Goodnotes
    with pytest.raises(Exception) as err:
        goodnotes("","one two three four")
    error_message = str(err.value)
    assert error_message == "Goodnotes entries must have title and contents"

""" Given a title and content
#formatted returns a formatted diary "My Title: These are the contents"
"""

def test_format_title_and_content():
    goodnotes = Goodnotes("My dairy","One Two Three Four")
    result = goodnotes.format()
    assert result == "My dairy: One Two Three Four"

""" Given a title and content
#count_words returns an int- numbers of words in title and contents
"""

def test_count_words_in_title_and_content():
    goodnotes= Goodnotes("My dairy","One Two Three four") 
    results = goodnotes.count_words()
    assert results == 4


""" Given a title and content
#reading_time returns the time estiamte to read the content. assuming wpm is 2
"""

def test_estimate_time_to_read_2_words_at_2_wpm(): 
    goodnotes = Goodnotes("My dairy","One Two") 
    results = goodnotes.reading_time(2)
    assert results == 1

""" Given a title and content
#reading_time returns the time estiamte to read the content. assuming wpm is 1
"""

def test_estimate_time_to_read_2_words_at_1_wpm(): 
    goodnotes = Goodnotes("My dairy","One Two") 
    results = goodnotes.reading_time(1)
    assert results == 2


""" Given a title and content
#reading_time returns the time estiamte to read the content. assuming wpm is 2
"""
def test_estimate_time_to_read_3_words_at_2_wpm(): 
    goodnotes = Goodnotes("My dairy","One Two Three") 
    results = goodnotes.reading_time(2)
    assert results == 2

# estimate_time_to_read_3_words_at_2_wpm(): ==> "My dairy: One Two" == 1.5 rounded up to 2

""" Given a title and content
#reading_time raises an exception error "WPM cannot be 0". assuming wpm is 0
"""
def test_estimate_time_to_read_3_words_at_0_wpm(): 
    goodnotes = Goodnotes("My dairy","One Two Three") 
    with pytest.raises(Exception) as err:
        goodnotes.reading_time(0)
    error_message = str(err.value)
    assert error_message == "WPM cannot be 0"


"""
Given a contents of six words
and a wpm of 2
and mintues of 1
#reading_chunk returns the first two words eg "one two three four five six" 
returns "one two"
"""
def test_reading_chunk_of_six_words_with_2_wpm_in_1_minute():
    goodnotes = Goodnotes("My dairy","One Two Three four five six")
    results = goodnotes.reading_chunk(2, 1)
    assert results == "One Two"

"""
Given a contents of six words
and a wpm of 2
and mintues of 2
#reading_chunk returns the first four words eg "one two three four five six" 
returns "one two three four"
"""

def test_reading_chunk_of_six_words_with_2_wpm_in_2_minute():
    goodnotes = Goodnotes("My dairy","One Two Three four five six")
    results = goodnotes.reading_chunk(2, 2)
    assert results == "One Two Three four"


"""
Given a contents of six words
and a wpm of 2
and mintues of 1
First time call #reading_chunk returns the first two words "one two"
second time call #reading_chunk(assert diary_entry.reading_chunk(1, 1)) returns the next word2 "three"-> making it more rigrous
third time call #reading_chunk returns the next two words "five six"
"""


def test_reading_chunk_with_two_wpm_and_one_minute_called_multiple_times():
    goodnotes = Goodnotes("My dairy","One Two Three four five six")
    first_call = goodnotes.reading_chunk(2, 1)
    second_call = goodnotes.reading_chunk(1, 1)
    third_call = goodnotes.reading_chunk(2, 1)
    assert first_call == "One Two"
    assert second_call == "Three"
    assert third_call == "four five"


"""
Given a contents of six words
If #reading_chunk is called repeatedly 
The last chuck is the last word in the text, even if shorter than could be read
the next chunk after that is at the start again
"""


def test_reading_chunk_wraps_around_on_multiple_calls():
    goodnotes = Goodnotes("My dairy","One Two Three four five six")
    first_call = goodnotes.reading_chunk(2, 2)
    second_call = goodnotes.reading_chunk(2, 2)
    third_call = goodnotes.reading_chunk(2, 2)
    assert first_call == "One Two Three four"
    assert second_call == "five six"
    assert third_call == "One Two Three four"



"""
Given a contents of six words
If #reading_chunk is called repeatedly with an exact ending
The last chuck is the last word in the text, even if shorter than could be read
the next chunk after that is at the start again
"""


def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    goodnotes = Goodnotes("My dairy","One Two Three four five six")
    first_call = goodnotes.reading_chunk(2, 2)
    second_call = goodnotes.reading_chunk(2, 1)
    third_call = goodnotes.reading_chunk(2, 2)
    assert first_call == "One Two Three four"
    assert second_call == "five six"
    assert third_call == "One Two Three four"