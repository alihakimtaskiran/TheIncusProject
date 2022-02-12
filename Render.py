import numpy as np
from scipy.io.wavfile import read, write
import scipy.signal as sps
import os
pi=np.math.pi
class Continuum(object):
    def __init__(self,entity,sample_rate=44100, pix_len=1):
        if not (type(entity)==tuple or type(entity)==list):
            raise TypeError("entity must be a tuple or a list")
        if not len(entity)==4:
            raise ValueError("entity must be in the form of (time,x,y,z)")
        if not type(sample_rate)==int:
            raise TypeError("sample_rate must be an integer")
        if sample_rate==0:
            raise ValueError("You must sample the entity at least once")
        if not sample_rate>0:
            raise ValueError("sample_rate must be bigger than 0")
        self.__entity=(int(entity[0]*sample_rate),)+entity[1:]
        for i in self.__entity:
            if not type(i)==int:
                raise TypeError("Entity is quantized.")
        self.__func=[]
        self.__play_list=[]
        self.__sample_rate=sample_rate
        

    def monotonicSpeaker(self, location, time_interval, amplitude, frequency, phase=1.5*pi):
        self.__func.append((np.array(location), time_interval, amplitude, frequency, phase))
        self.__config_amplitudes()
        
    def hear(self,location):
        if not (type(location)==tuple or type(location)==list):
            raise ValueError("location must be a tuple or a list")
        if not len(location)==3:
            raise ValueError("location must be in the form of (x,y,z)")
        for i in range(3):
            if self.__entity[i+1]<=location[i]:
                print(self.__entity[i]<=location[i])
                raise ValueError("No such location exists in continuum")
        sw=np.zeros(self.__entity[0])

        location=np.array(location)
        for src in self.__func:
            
            r=np.linalg.norm(src[0]-location)
            ____=r/330
            perm_iter_start=(____+src[1][0])*self.__sample_rate
            perm_iter_stop=(____+src[1][1])*self.__sample_rate
            for i in range(len(sw)):
                ______=0
                if perm_iter_stop>i>perm_iter_start:
                    ω=2*pi*src[3]
                    ______+=src[2]*np.math.cos(ω*(0.0030303030303030303*r-i/self.__sample_rate)+src[4])/r**2
                sw[i]=______
        for msc in self.__play_list:
            if msc[2]*self.__sample_rate>self.__entity[0]:
                print(f"{msc[0]} doesn't start in the entity")
            else:
                sr,sound=read(msc[0])
                sound=sound.T[0]
                
                sound=sps.resample(sound, int(sound.shape[0]/sr)*self.__sample_rate)
                
                
                propagation_delay=int(np.linalg.norm(msc[1]-location)/330)*self.__sample_rate
            
            
                _______=msc[2]+propagation_delay
                if self.__entity[0]>_______+sound.shape[0]:
                    sw[_______:_______+sound.shape[0]]+=sound
                else:
                    sw[_______:]+=sound[:self.__entity[0]-_______]

        return sw


    def __config_amplitudes(self):
        the_biggest=0
        if not self.__func==[]:
            return None
        else:
            for i in range(len(self.__func)):
                if self.__func[i][2]>the_biggest:
                    the_biggest=self.__func[i][2]
            for i in range(len(self.__func)):
                self.__func[i][2]/=the_biggest
        return None
    
    def play_music(self,path_to_file,location,start_time):
        if not type(path_to_file)==str:
            raise ValueError("Path is a string")
        if not os.path.isfile(path_to_file):
            raise FileNotFoundError(f"No such file exists: {path_to_file}")
        self.__play_list.append((path_to_file,np.array(location),start_time))
