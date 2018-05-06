#This is Watchdog Test Program
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    # print(sys.argv[1])
    logging.basicConfig(filenmae='rishi.txt',level=logging.DEBUG,
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
print(logger.level)

# help(KeyboardInterrupt)
help(Observer)