import socket
import time
from pyfiglet import Figlet
import threading
from queue import Queue
from termcolor import colored

f = Figlet(font='standard')
print(colored(f.renderText('HSE Scanner'), 'red'))

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

ip_address = input('IP: ')
host = socket.gethostbyname(ip_address)
print('Scanning on IP: ', host)


def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = sock.connect((host, port))
        with lock:
            print(port, 'is open')
        con.close()
    except:
        pass


def execute():
    while True:
        worker = queue.get()
        scan(worker)
        queue.task_done()


queue = Queue()
start_time = time.time()

for x in range(100):
    thread = threading.Thread(target=execute)
    thread.daemon = True
    thread.start()

for worker in range(1, 500):
    queue.put(worker)

queue.join()

print(colored('Scan Finished', 'green'))
print(colored('Time Spent', 'green'), colored(time.time() - start_time, 'green'))
