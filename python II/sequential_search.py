class Music:
    def __init__(self, title, interpreter, composer, year):
        self.title = title
        self.interpreter = interpreter
        self.composer = composer
        self.year = year

class Search:

    def search_by_title(self, playlist, title):
        for i in range(len(playlist)):
            if playlist[i].title == title:
                return i
        return -1

    def lets_search(self, music_to_search):
        playlist = [
                    Music("Human", "Rag'n'Bone Man", "Rag'n'Bone Man", 2016),
                    Music("Down With The Sickness", "Disturbed", "RDisturbed", 2000),
                    Music("Aerials", "System Of A Down", "System Of A Down", 2011)
        ]

        finded = self.search_by_title(playlist, music_to_search)

        if finded == -1:
            print("The music ", music_to_search, " it's no present on current playlist!")
        else:
            index = playlist[finded]
            print(index.title, index.interpreter, index.composer, index.year, sep=", ")


s = Search()
s.lets_search("Aerials")