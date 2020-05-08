import psutil
import subprocess

class mplayer:
    def __init__(self,station,stream):
        self.station = station
        self.stream = stream

    def play(self):
        print(self.station)
        print(self.stream)
        command = ['mplayer',self.stream]
        subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    def stop(self):
        mplayer_pid = [proc.pid for proc in psutil.process_iter() if proc.name() == 'mplayer']
        print(mplayer_pid)
        for mpid in mplayer_pid:
            print('stop' + ' ' + str(mpid))
            command = ['kill','-9',str(mpid)]
            subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
'''
stream = 'https://playerservices.streamtheworld.com/api/livestream-redirect/KITSFM_TLRAAC.aac'
from mp import mplayer
test = mplayer('live105',stream)
test.play()
test.stop()
'''



