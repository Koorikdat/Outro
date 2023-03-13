import time
import os
import pygame as pg
from pygame import mixer


pg.init()
mixer.music.load('Outro.mp3')


def countdown (num):
    
    mixer.music.play(1)
     
    for i in range(0, num):
        print ('System shutting down in' , num - i)
        time.sleep(1)
    print ('life is a movie, and we are the audience')
    os.system("shutdown /s /t 1")
    print ('peace')
    
    
    
    
countdown(17)
    
        
     
    