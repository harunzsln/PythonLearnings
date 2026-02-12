from random import choice

class MP3player():
    def __init__(self, songList = []):
        self.playingSongName = ""
        self.volume = 100
        self.songList = songList
        self.status = True  

    def chooseSong(self):
        counter = 1
        for song in self.songList:
            print("{}. {}".format(counter, song))
            counter += 1

        chooseSong = int(
            input("Please enter the number of the song you want to choose : "))

        while chooseSong < 1 or chooseSong > len(self.songList):
            chooseSong = int(
                input("Invalid value, please enter a number within the given range (1-{}) : ".format(len(self.songList))))
        self.playingSongName = self.songList[chooseSong - 1]

    def increaseVolume(self):
        if self.volume == 100:
            pass
        else:
            self.volume += 10

    def decreaseVolume(self):
        if self.volume == 0:
            pass
        else:
            self.volume -= 10

    def randomSong(self):
        randomSong = choice(self.songList)
        self.playingSongName = randomSong

    def addSong(self):
        singerName = input("Please enter the singer's name : ")
        songName = input("Please enter the song's name : ")

        self.songList.append(singerName + " - " + songName)

    def removeSong(self):
        counter = 1
        for song in self.songList:
            print("{}. {}".format(counter, song))
            counter += 1
        deleteSongNumber = int(input("Please enter the number of the song you want to delete : "))

        while deleteSongNumber < 1 or deleteSongNumber > len(self.songList):
            deleteSongNumber = int(input("Invalid value, please enter a number within the given range (1-{}) : ".format(len(self.songList))))
        self.songList.pop(deleteSongNumber - 1)

    def closePlayer(self):
        self.status = False

    def showMenu(self):
        print("""
Song List : {}
Playing Song : {}
Volume : {}
1)Choose Song
2)Increase Volume
3)Decrease Volume
4)Random Song
5)Add Song
6)Remove Song
7)Close Player
""".format(self.songList, self.playingSongName, self.volume))

    def chooseMenuOption(self):
        choose= int(input("Please choose an option : "))

        while choose < 1 or choose > 7:
            choose = int(input("Invalid value, please choose an option within the given range (1-7) : "))

        return choose

    def runPlayer(self):
        self.showMenu()
        chooseMenuOption = self.chooseMenuOption()

        if chooseMenuOption == 1:
            self.chooseSong()

        if chooseMenuOption == 2:
           self.increaseVolume()

        if chooseMenuOption == 3:
            self.decreaseVolume()

        if chooseMenuOption == 4:
            self.randomSong()

        if chooseMenuOption == 5:
            self.addSong()

        if chooseMenuOption == 6:
            self.removeSong()    

        if chooseMenuOption == 7:
            self.closePlayer()


mp3player = MP3player()
while mp3player.status:
    mp3player.runPlayer()

print("Player closed. Goodbye!")
