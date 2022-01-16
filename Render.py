import numpy as np
from scipy.io.wavfile import write
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
        if self.__func==[]:
            return sw
        location=np.array(location)
        for src in self.__func:
            r=np.linalg.norm(src[0]-location)
            perm_iter_start=(r/330+src[1][0])*self.__sample_rate
            perm_iter_stop=(r/330+src[1][1])*self.__sample_rate
            for i in range(len(sw)):
                if perm_iter_stop>i>perm_iter_start:
                    ω=2*pi*src[3]
                    sw[i]+=src[2]*np.math.cos(ω*(0.0030303030303030303*r-i/self.__sample_rate)+src[4])/r**2
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
