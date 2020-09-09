#look up threading and queue in the python documentation
# https://en.wikibooks.org/wiki/Python_Programming/Threading


import threading
import time

# def loop1_10():
#     for i in range(1, 11):
#         time.sleep(1)
#         print(i)

# threading.Thread(target=loop1_10).start()


class MyThread(threading.Thread):
    def run(self):                                         # Default called function with mythread.start()
        print("{} started!".format(self.getName()))        # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))       # "Thread-x finished!"

def main():
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, run method will be invoked
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another

if __name__ == '__main__':
    main()
