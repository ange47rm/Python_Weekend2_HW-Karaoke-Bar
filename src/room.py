class Room ():
    
    def __init__ (self, music_genre):
        self.music_genre = music_genre
        self.guests = []    # list of Guest objects
        self.guest_capacity = 5
        self.songs_playlist = []    # list of Song objects
  
    def check_in_guest (self, guest):
        self.guests.append (guest)

    def check_out_guest (self, guest):
        self.guests.remove (guest)

    def add_song_to_room_playlist (self, song):
        self.songs_playlist.append (song)

    def remove_song_from_room_playlist (self, song):
        self.songs_playlist.remove (song)

    def clear_music_playlist (self, Room):
        self.songs_playlist.clear()


        
        



    



        
