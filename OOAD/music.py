# Write a program that simulates a music streaming service. The program should have classes for songs,
# albums, and playlists. Songs should have attributes such as title, artist, and length. Albums should
# have attributes such as title, artist, and release date. Playlists should have attributes such as name
# and songs included. The program should allow users to search for and listen to songs, create and manage
# playlists, and view their listening history. Use interfaces to implement classes for different types of 
# music (e.g., rock, pop) and abstract classes for music operations.

from abc import ABC, abstractmethod
class Songs(ABC):
    def __init__(self, title, artist,lenght) -> None:
        self.__title = title
        self.__artist = artist
        self.__lenght = lenght
    @abstractmethod
    def genre(self):
        ...
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,value):
        if value == "":
            raise ValueError("Can't be empty...")
        self.__title = value
    @property
    def artist(self):
        return self.__artist
    @artist.setter
    def artist(self,value):
        if value == "":
            raise ValueError("Can't be empty...")
        self.__artist = value
    @property
    def lenght(self):
        return self.__lenght
    @lenght.setter
    def lenght(self,value):
        if value <= 0 :
            raise ValueError("Lenght can't be negative...")
        self.__lenght = value
    
class Pop(Songs):
    def __init__(self, title, artist, lenght) -> None:
        super().__init__(title, artist, lenght)
    def genre(self):
        print("Pop music...")
class Rock(Songs):
    def __init__(self, title, artist, lenght) -> None:
        super().__init__(title, artist, lenght)
    def genre(self):
        print("Rock music...")

class Albums:
    def __init__(self,title, artist, release_date) -> None:
        self.__title = title
        self.__artist = artist
        self.__release_date = release_date
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,value):
        if value == "":
            raise ValueError("Can't be empty...")
        self.__title = value
    @property
    def artist(self):
        return self.__artist
    @artist.setter
    def artist(self,value):
        if value == "":
            raise ValueError("Can't be empty...")
        self.__artist = value

class Playlists:
    def __init__(self,name) -> None:
        self.__name = name
        self.included_songs = []
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == "":
            raise ValueError("Can't be empty...")
        self.__name = value
    def add_songs(self, song:Songs):
        if isinstance(song,Songs):
            self.included_songs.append(song)
            print(f'{song.artist} - {song.title} added to {self.__name}')
    
class User:
    def __init__(self,name) -> None:
        self.__name = name
        self.__playlist = []
        self.__listening_history = []
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == "":
            raise ValueError("Can't be empty...")
        self.__name = value
    
    def search_songs(self,playlist:Playlists,song: Songs):
        if playlist.name in self.__playlist:
            if isinstance(song,Songs) and song in playlist.included_songs:
                print(f"Yes, there is {song.artist} - {song.title}")
            else:
                print("Couldn't find song...")
    
    def listen_songs(self,playlist: Playlists, song: Songs):
        if song in playlist.included_songs:
            if isinstance(song,Songs):
                print(f"Playing {song.artist} - {song.title} ...")
                tmp = str(song.artist) +str(" - ")+ str(song.title)
                self.__listening_history.append(tmp)
        else:
            print("Couldn't find song...")
    
    def add_playlist(self,playlist: Playlists):
        self.__playlist.append(playlist.name)
        print(f"{self.__name} added '{playlist.name}'.")

    def view_playlist(self):
            print(f"{self.__name}'s playlists are ...")
            for item in self.__playlist:
                print(f'~ {item}')
    def view_history(self):
        print(f"This is {self.__name} listening history. ")
        for i in self.__listening_history:
            print(i)



wk = Pop("The Hills","Weekend", 3.23)
wk1 = Rock("Timezone","Maneskin", 3.40)

pl = Playlists("My first playlist")
pl1 = Playlists("My second playlist")

bob = User("Bob")
bob.add_playlist(pl)
bob.add_playlist(pl1)

pl.add_songs(wk)
pl.add_songs(wk1)

bob.view_playlist()
bob.listen_songs(pl,wk)
bob.search_songs(pl,wk)
bob.listen_songs(pl,wk1)
bob.search_songs(pl1,wk)

bob.view_history()