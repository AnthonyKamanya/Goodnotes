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
        if self._notes == [] or wpm ==0 :
            raise Exception("Cannot Estimate reading time for no entry or 0 wpm")
        return math.ceil(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._notes == [] or wpm ==0 :
            raise Exception("Cannot Estimate reading time for no entry or 0 wpm")
        words_the_user_can_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for each_readable_entry in self._notes:
            if each_readable_entry.count_words() <= words_the_user_can_read:
                if each_readable_entry.count_words() > longest_found_so_far:
                    most_readable = each_readable_entry
                    longest_found_so_far = each_readable_entry.count_words()
        return most_readable
                

