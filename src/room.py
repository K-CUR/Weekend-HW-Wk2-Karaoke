class Room:
        def __init__(self, room_name, entry_fee, max_capacity):
            self.room_name = room_name
            self.entry_fee = entry_fee
            self.max_capacity = max_capacity
            self.guest_list = []
            self.song_list = []

        def check_in_guest(self, guest, room):
            room.guest_list.append(guest.name)

        def check_out_guest(self, guest, room):
            room.guest_list.remove(guest.name)

        def add_song_to_room(self, song, room):
            room.song_list.append(song.title)

        