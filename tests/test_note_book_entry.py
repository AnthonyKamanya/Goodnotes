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

"""
When I Initialize with five word contents 
then #reading time with wpm of 2 should return 3
"""

def test_reading_time():
    note_entry = DiaryEntry("first entry","Youtube Rental AmazonFBA dropshipping software_company")
    result = note_entry.reading_time(2)
    assert result == 3

"""
When I initialise with a five-word contents
then, at first, reading_chunk should return the first chunk 
readable in the time
"""

def test_readable_chunk_first_chunk():
    note_entry = DiaryEntry("first entry","Youtube Rental AmazonFBA dropshipping software_company")
    results = note_entry.reading_chunk(2,1)
    assert results == "Youtube Rental"


"""
When I initialise with a five-word contents
then, on the second call, reading_chunk should return the second chunk 
readable in the time
"""

def test_readable_chunk_second_chunk():
    note_entry = DiaryEntry("first entry","Youtube Rental AmazonFBA dropshipping software_company")
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    assert results == "AmazonFBA dropshipping"



"""
When I initialise with a five-word contents
then, on the third call, reading_chunk should return the third chunk 
readable in the time
"""

def test_readable_chunk_third_chunk():
    note_entry = DiaryEntry("first entry","Youtube Rental AmazonFBA dropshipping software_company")
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    assert results == "software_company"

"""
When I initialise with a five-word contents
then, on the fourth call, reading_chunk should start again from the beginning 
readable in the time
"""

def test_readable_chunk_fourth_chunk():
    note_entry = DiaryEntry("first entry","Youtube Rental AmazonFBA dropshipping software_company")
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    assert results == "Youtube Rental"


"""
When I initialise with a six-word contents
then, on the fourth call, reading_chunk should start again from the beginning 
readable in the time
"""

def test_readable_chunk_fourth_chunk_with_exact_chunks():
    note_entry = DiaryEntry("first entry","Youtube Rental AmazonFBA dropshipping software_company travle_agency")
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    results = note_entry.reading_chunk(2,1)
    assert results == "Youtube Rental"