import os
import subprocess
import time
import math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

os.chdir(r"C:/Users/Lineamingo/Desktop/cosas_U/cripto/tarea4/hashcat/hashcat-6.1.1")
hash_cat = "hashcat -a 0 -m 1800 ../../hashes/archivo_5 ../../diccionarios/diccionario_2.dict -o output.txt --potfile-disable -d 2" 
#cambiar ../../hashes/archivo_n por la dirección y el nombre del hash que se quiera usar

start = time.time()
h = subprocess.Popen(hash_cat, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
end = time.time()


f = open("output.txt", "r")
ff = f.read()

hash_result = []
for word in ff.split():
    x = word.split(":")
    hash_result.append(x[1])
    #x[1] para archivo_1 y archivo_4, x[2] para archivo_2 y archivo_3

f.close()
os.remove("output.txt")

os.chdir(r"C:/Users/Lineamingo/Desktop/cosas_U/cripto/tarea4")
result = open("hashes_crackeados_5.txt", "w")
#dependiendo del archivo elegido, cambiar el numero de hashes_crackeados_n
for i in hash_result:
    result.write(i+'\n')
result.close()



total_time = (end - start)
if total_time<60:
    print("Operación terminada en: ", truncate(total_time, 2), " segundos.")
elif total_time>=60 and total_time<3600:
    print("Operación terminada en: ", truncate(total_time/60, 2), " minutos.")
else:
    print("Operación terminada en: ", truncate(total_time/3600, 2), " horas.")


