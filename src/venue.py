class Venue:
        
    def __init__(self, till):
        self.till = till


    def add_entry_to_till(self, room):
        self.till += room.entry_fee