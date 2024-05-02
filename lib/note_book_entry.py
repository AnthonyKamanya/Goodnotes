import math
class DiaryEntry:
    
    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents

    def count_words(self):
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        return math.ceil(self.count_words()/wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass