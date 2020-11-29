from src.song import Song 

class Guest ():
    
    def __init__ (self, name, money, song):
        self.name = name
        self.money = money
        self.song = song

    def cheer_loudly_or_be_disappointed (self, room):
        if self.song in room.songs_playlist:
            return "Whooo!!!"
        else:
            return "This playlist is lame!"

    