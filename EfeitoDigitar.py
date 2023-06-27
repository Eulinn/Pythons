import time, sys


def Printer(Text,temp=0.1,BL=False):
    for i in list(Text):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(temp)

    print() if BL else None

