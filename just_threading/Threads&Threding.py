import os
from time import sleep
from threading import Thread


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

    boxthread = Thread(target=box)
    ledthread = Thread(target=led)
    boxthread.daemon = True
    ledthread.daemon = True

    boxthread.start()
    ledthread.start()

    while (True):
        pass


if __name__ == "__main__":
    main()
