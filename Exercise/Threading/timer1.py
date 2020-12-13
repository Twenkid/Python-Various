#Author: Todor Arnaudov, 13.12.2020
#Answer to: https://stackoverflow.com/questions/65271284/how-to-create-a-timer-function-that-can-be-called-multiple-times-before-it-ends/65271375#65271375

from threading import Timer

def hello(t):
    print("Counted to", t)

t1 = Timer(4, hello, [4])
t1.start()
t2 = Timer(1, hello, [1])
t2.start()
t3 = Timer(3, hello, [3])
t3.start()

'''
t1 = threading.Thread.Timer(4, hello, [4])
t1.start()
t2 = threading.Thread.Timer(1, hello, [1])
t2.start()
t3 = threading.Thread.Timer(3, hello, [3])
t3.start()
'''