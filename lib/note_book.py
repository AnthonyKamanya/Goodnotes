import math
class Diary:
    def __init__(self):
        self._notes = []

    def add(self, entry):
       self._notes.append(entry)

    def all(self):
        return self._notes

    def count_words(self):
        total = 0
        for notes in self._notes:
            total += notes.count_words()
        return total
        
        

    def reading_time(self, wpm):
        return math.ceil(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass

