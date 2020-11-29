class Room ():
    
    def __init__ (self, music_genre):
        self.music_genre = music_genre
        self.guests = []    # list of Guest objects
        self.guest_capacity = 5
        self.songs_playlist = []    # list of Song objects
        self.till = 0
        self.entry_fee = 25
  
    def check_in_guest (self, guest):
        if len(self.guests) < self.guest_capacity and guest.money >= self.entry_fee:
            self.guests.append (guest)
            self.till += self.entry_fee
            guest.money -= self.entry_fee
        else:
            return "Guest not allowed in. Room is currently full or guest has not enough money."        

    def check_out_guest (self, guest):
        self.guests.remove (guest)

    def add_song_to_room_playlist (self, song):
        self.songs_playlist.append (song)

    def remove_song_from_room_playlist (self, song):
        self.songs_playlist.remove (song)

    def clear_music_playlist (self, Room):
        self.songs_playlist.clear()
        



    



        
