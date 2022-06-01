
from time import*
from threading import Thread

def box ():
    while True:
        print("my box is open")
        sleep(5)
        print("my box is close")
        sleep(5)

def led():
    while True:
        print("my led is on")
        sleep(2)
        print("my led is off")
        sleep(2)


boxthread = Thread(target = box)
ledthread = Thread(target = led)
boxthread.daemon = True
ledthread.daemon = True

boxthread.start()
ledthread.start()

while(True):
    pass


