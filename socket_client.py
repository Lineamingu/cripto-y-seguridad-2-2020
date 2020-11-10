from Crypto.Util.number import *
from Crypto import Random
import random
import Crypto
import libnum
import sys
import math
import socket
import pickle
import time
import math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

m=10
bits=2000

if (len(sys.argv)>1):
    m=(sys.argv[1])

if (len(sys.argv)>2):
    bits=int(sys.argv[2])

q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
bits=bits/4
g = random.randint(1,2**bits) #public key
#---------------------------------------
dirr = "./hashes_generados_5.txt"
#---------------socket------------------
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
HEADERSIZE = 10

start = time.time()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    d = [dirr, g]
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    s.sendall(msg)
    data = s.recv(1024)
    if data:
        new_data = pickle.loads(data[HEADERSIZE:])
        dirr1 = new_data[0]
        dirr2 = new_data[1]
end = time.time()

total_time = (end - start)
if total_time<60:
    print('Archivos: ', dirr1, 'y ', dirr2, ' creados luego de: ', truncate(total_time, 2), " segundos.")
elif total_time>=60 and total_time<3600:
    print('Archivos: ', dirr1, 'y ', dirr2, ' creados luego de: ', truncate(total_time/60, 2), " minutos.")
else:
    print('Archivos: ', dirr1, 'y ', dirr2, ' creados luego de: ', truncate(total_time/3600, 2), " horas.")

