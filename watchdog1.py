#This is Watchdog Test Program
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    # print(sys.argv[0])
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(message)s')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
#This will give you the logging details of the directory in your editor

# Usage and Running
''' 1. Goto your command prompt or editor you are using
    2.open watchdog1.py file containg folder
    3.use 'python watchdog1.py'  #without quotations
    4. Try to make changes in files of your directory, Now you will able to see the log in command prompt itself 
'''


#if you want to create the logging details in a new document say 'mylogging.log' we can do that also as follows


import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    # print(sys.argv[0])
    logging.basicConfig(filename ='mylogging.log',level=logging.DEBUG,
                        format='%(asctime)s - %(message)s',filemode='a')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
# Usage and Running
''' 1. Goto your command prompt or editor you are using
    2.open watchdog1.py file containg folder
    3.use 'python watchdog1.py'  #without quotations
    4. Try to make changes in files of your directory
    5. Now open your directory and find 'mylogging.log' which have all your logging details
    '''

'''Note:
if you want to keep all the logs in 'mylogging.log', you can keep the filemode as 'a'(in line 46)
or if you don't want to keep logs then you can change filemode.
I hope you are aware of file operations, like
                                            r,
                                            r+,
                                            w,
                                            w+,
                                            a,
                                            a+  modes.
Happy Coding!
'''


    

