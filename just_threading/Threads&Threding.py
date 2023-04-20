import os
from threading import Thread
from time import sleep


def main():
    def box():
        while True:
            print(os.getpid())
            print("my box is open")
            sleep(5)
            print("my box is close")
            sleep(5)

    def led():
        while True:
            print(os.getpid())
            print("my led is on")
            sleep(2)
            print("my led is off")
            sleep(2)

    boxThread = Thread(target=box)
    ledThread = Thread(target=led)
    boxThread.daemon = True
    ledThread.daemon = True

    boxThread.start()
    ledThread.start()

    while True:
        pass


if __name__ == "__main__":
    main()
