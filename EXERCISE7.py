#**************HEALTHY PROGRAMMER***************

#3.5 WATER- WATER.MP3 PLAY
#then input of stopping and store time of
# drinking water in txt file
# PHYSICAL EXERCISE after every 45 MIN  PHYSICAL.MP3  log
# time= 9am to 5pm
#  AFTER 30 MIN EYE EXERCISE  EYE.MP3 and input done  log


#pygame to play music

# def gettime():
#     import datetime
    # return datetime.datetime.now()

# from pygame import mixer
# # file="water.mp3"
# mixer.init()#starting the mixer
# mixer.music.load("water.mp3")#loading the song
# mixer.music.set_volume(0.7)#stteing volume
# mixer.music.play()#start playing the song
#
# #_____________WATER________________
# import time
# initial=time.time()
# for i in range(0,10):
#     mixer.init()  # starting the mixer
#     mixer.music.load("water.mp3")  # loading the song
#     mixer.music.set_volume(0.7)  # stteing volume
#     mixer.music.play()  # start playing the song
#     i+=1

#
# #___________EYE________
# from pygame import mixer
# from datetime import datetime
# import time
# for i in range(0,10):
#     initial=time.time()
#     time.sleep(2)
#     mixer.init()
#     mixer.music.load("water.mp3")
#     mixer.music.set_volume(0.7)
#     var1=input("do eye exercise for 2 min\n")
#     f=open("ee","a")
#     var2=input("if exercise is done type done")
#     mixer.music.stop()
#     var3=f.write(time.asctime(time.localtime(time.time())),var2)
#     continue




from pygame import mixer
import time
from datetime import datetime
def eye(file,stopper):
    time.sleep(1800)
    initial=time.time()
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while(1):
        var1=input("enter yes if eye exercise in done")
        if var1==stopper:
            mixer.music.stop()
            f=open("eye","a")
            var3 = f.write(time.asctime(time.localtime(time.time())), var2)
            break
