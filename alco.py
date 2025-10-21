__author__='andre'
import string,datetime,configparser

class Alko:
    def __init__(self,weight,start_time):
        self.__delta__=50
        self.__ratio__=3.4
        self.__volume=0
        self.__weight=weight
        self.__start_time=start_time
        print(self.__start_time)
        pass
    def drink(self,volume):
        self.__volume+=volume
    def volume(self):
        return self.__volume
    def duration(self):
        if self.__volume>0:
            if self.__volume<self.__delta__:
                delta=self.__volume
            else:
                delta=self.__delta__
            
            return (self.__volume+delta)*self.__ratio__/self.__weight
        else:
            return 0

import datetime,configparser
a=Alko

me=Alko(115,datetime.datetime.now ())

while True:
    vt=input('давай ёбнем:')
    if vt.isnumeric() and int(vt)>0:
        me.drink(int(vt))
    else:
        break

print(me.volume())
print(me.duration())
print("alco")
