# Develop a log monitoring system for a web server. The system should read and analyze server logs in real-time.
# New log entries are appended to a file continuously, and your goal is to monitor the log file for specific error keywords.
# Create a thread that reads new lines added to the log file continuously.
# Create another thread that checks if any new line contains the keyword “ERROR” and prints it to the console.
# Both threads should run concurrently without blocking each other, using shared data structures like queues to communicate.

file = "server_log.txt"

from threading import Thread

def read_and_add(file_path: str):
  read = open(file_path,mode = "r")
  for i in read.readlines():
    print(f"Added to the Log file : {i}")
  read.close()

def error_check(file_path: str):
  read = open(file_path,mode = "r")
  for i in read.readlines():
    if "error".upper() in i.upper():
      print(f"There is an ERROR message in : {i}")
  read.close()


if __name__ == '__main__':
  
  thread1 = Thread(target=read_and_add, args=(file, ))
  thread2 = Thread(target=error_check, args=(file, ))

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()