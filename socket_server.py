from Crypto.Util.number import *
from Crypto import Random
import random
import Crypto
import libnum
import sys
import math
import socket
import pickle

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
HEADERSIZE = 10
#-------------------------------------------------------
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Conexión desde: ', addr)
            while True:
                data = conn.recv(1024)
                if data:
                    new_data = pickle.loads(data[HEADERSIZE:])
                    dirr = new_data[0]
                    f = open(dirr, "r")
                    ff = f.read()
                    new_cyp = []
                    new_decyp = []
                    for word in ff.split():

                        m=10
                        bits=2000  #default: 512

                        if (len(sys.argv)>1):
                            m=(sys.argv[1])

                        if (len(sys.argv)>2):
                            bits=int(sys.argv[2])

                        msg=word
                        m=  bytes_to_long(msg.encode('utf-8'))
                        q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
                        bits=bits/4

                        f=random.randint(1,2**bits) #llave privada
                        g=random.randint(1,2**bits) #llave publica

                        while gcd(f, g)>1:
                            g=random.randint(1,2**bits)

                        h=(libnum.invmod(f, q)*g) % q

                        #print ("Number of bits in q=%d" % bits)
                        #print ("====Private key====\nf=%d" % f)
                        #print ("q=%d" % q)
                        #print ("\n====Public key====\ng=%d" % g)
                        #print ("\nh=%d" % h)
                        #print ("\nq=%d" % q)

                        r=random.randint(1,2**64)
                        e=(r*h+m) % q #mensaje cifrado
                        new_cyp.append(str(e))
                        a =(f*e) %q
                        b = (libnum.invmod(f, g)*a) % g
                        byte_b = long_to_bytes(b)
                        dec_msg = byte_b.decode('utf-8') #mensaje descifrado
                        new_decyp.append(dec_msg)
                    
                    result = open("hashes_cifrados_5.txt", "w")
                    for i in new_cyp:
                        result.write(i+'\n')
                    result.close()
                    new_dirr1 = "./hashes_cifrados_5.txt"

                    result = open("hashes_descifrados_5.txt", "w")
                    for j in new_decyp:
                        result.write(j+'\n')
                    result.close()
                    new_dirr2 = "./hashes_descifrados_5.txt"

                    d = [new_dirr1, new_dirr2]
                    new_dirrs = pickle.dumps(d)
                    new_dirrs = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+new_dirrs

                if not data:
                    break
                conn.sendall(new_dirrs)