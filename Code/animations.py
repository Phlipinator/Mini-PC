from machine import Pin, SPI
from max7219 import Max7219
import time

# Initialisation
spi = SPI(1, baudrate=10000000)
screen = Max7219(8, 8, spi, Pin(15))

waitTime = 0.3
waitTimeShort = 0.1
    
def display(animation): 
    if animation == "heart":
        heart()
    elif animation == "smile":
        smile()
    elif animation == "sad":
        sad()
    elif animation == "received":
        received()
    else:
        print("Unhandeled animation")      
            
def heart():
    heartOne()
    time.sleep(waitTime)
    heartTwo()
    time.sleep(waitTime)
    heartThree()
    time.sleep(waitTime)
    heartFour()
    time.sleep(waitTime)
    heartFive()
    time.sleep(waitTime)
    heartFour()
    
def heartOne():
    screen.fill(0)
    screen.hline(2,3,2,1)
    screen.hline(2,4,2,1)
    screen.show()
    
def heartTwo():
    screen.fill(0)
    screen.hline(1,3,4,1)
    screen.hline(1,4,4,1)
    screen.hline(2,2,2,1)
    screen.hline(2,5,2,1)
    screen.show()
    
def heartThree():    
    screen.fill(0)
    screen.hline(3,0,2,1)
    screen.hline(2,1,4,1)
    screen.hline(1,2,5,1)
    screen.hline(0,3,5,1)
    screen.hline(0,4,5,1)
    screen.hline(1,5,5,1)
    screen.hline(2,6,4,1)
    screen.hline(3,7,2,1)
    screen.show()

def heartFour():    
    screen.fill(0)
    screen.hline(4,0,2,1)
    screen.hline(3,1,4,1)
    screen.hline(2,2,5,1)
    screen.hline(1,3,5,1)
    screen.hline(1,4,5,1)
    screen.hline(2,5,5,1)
    screen.hline(3,6,4,1)
    screen.hline(4,7,2,1)
    screen.show()
    
def heartFive():    
    screen.fill(0)
    screen.hline(5,0,2,1)
    screen.hline(4,1,4,1)
    screen.hline(3,2,5,1)
    screen.hline(2,3,5,1)
    screen.hline(2,4,5,1)
    screen.hline(3,5,5,1)
    screen.hline(4,6,4,1)
    screen.hline(5,7,2,1)
    screen.show()


def smile():
    smileOne()
    time.sleep(waitTimeShort)
    smileTwo()
    time.sleep(waitTimeShort)
    smileThree()
    time.sleep(waitTimeShort)
    smileFour()
    time.sleep(waitTimeShort)
    smileFive()
    time.sleep(waitTimeShort)
    smileSix()
    time.sleep(waitTimeShort)
    smileSeven()
    time.sleep(waitTime)
    smileEight()
    time.sleep(waitTime)
    smileSeven()
    
def smileOne():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.show()

def smileTwo():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.vline(2,2,1,1)
    screen.show()
    
def smileThree():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.vline(2,2,2,1)
    screen.show()

def smileFour():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.vline(2,2,3,1)
    screen.show()
    
def smileFive():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.vline(2,2,4,1)
    screen.show()
    
def smileSix():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.vline(2,2,4,1)
    screen.pixel(3,6,1)
    screen.show()
    
def smileSeven():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.vline(2,2,4,1)
    screen.pixel(3,6,1)
    screen.hline(5,2,2,1)
    screen.hline(5,5,2,1)
    screen.show()
    
def smileEight():
    screen.fill(0)
    screen.pixel(3,1,1)
    screen.vline(2,2,4,1)
    screen.pixel(3,6,1)
    screen.pixel(5,2,1)
    screen.pixel(5,5,1)
    screen.show()
    
    
def sad():
    sadOne()
    time.sleep(waitTimeShort)
    sadTwo()
    time.sleep(waitTimeShort)
    sadThree()
    time.sleep(waitTimeShort)
    sadFour()
    time.sleep(waitTimeShort)
    sadFive()
    time.sleep(waitTimeShort)
    sadSix()
    time.sleep(waitTimeShort)
    sadSeven()
    time.sleep(waitTime)
    sadEight()
    time.sleep(waitTime)
    sadSeven()
    
def sadOne():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.show()
    
def sadTwo():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.vline(2,2,1,1)
    screen.show()

def sadThree():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.vline(2,2,2,1)
    screen.show()

def sadFour():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.vline(2,2,3,1)
    screen.show()
    
def sadFive():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.vline(2,2,4,1)
    screen.show()
    
def sadSix():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.vline(2,2,4,1)
    screen.pixel(1,6,1)
    screen.show()
    
def sadSeven():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.vline(2,2,4,1)
    screen.pixel(1,6,1)
    screen.hline(5,2,2,1)
    screen.hline(5,5,2,1)
    screen.show()
    
def sadEight():
    screen.fill(0)
    screen.pixel(1,1,1)
    screen.vline(2,2,4,1)
    screen.pixel(1,6,1)
    screen.pixel(5,2,1)
    screen.pixel(5,5,1)
    screen.show()

def received():
    screen.fill(0)
    screen.pixel(3,0,1)
    screen.pixel(2,1,1)
    screen.pixel(1,2,1)
    screen.pixel(2,3,1)
    screen.pixel(3,4,1)
    screen.pixel(4,5,1)
    screen.pixel(5,6,1)
    screen.pixel(6,7,1)
    screen.show()