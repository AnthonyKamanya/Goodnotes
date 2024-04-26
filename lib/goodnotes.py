import math

class Goodnotes():

    def __init__(self, title, content):
        if title == "" or content == "":
            raise Exception("Goodnotes entries must have title and contents")
        
        self.title = title
        self.content = content
        self.read_so_far = 0
        

    def format(self):
        return f"{self.title}: {self.content}"
    
    def count_words(self):
        words_split = self.content.split(" ")
        return len(words_split)
    
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("WPM cannot be 0")
        
        est_reading_time = self.count_words()/wpm
        return math.ceil(est_reading_time)
    
    def reading_chunk(self,wpm,minutes):
        number_of_words_to_read = wpm * minutes
        words = self.content.split(" ")
        if self.read_so_far >= len(words):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end =self.read_so_far + number_of_words_to_read
        chunk_words = words[chunk_start : chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)
        


        
