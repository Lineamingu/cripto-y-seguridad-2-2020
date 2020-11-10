import bcrypt
import time
import math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

f = open("hashes_crackeados_5.txt", "r")
ff = f.read()

start = time.time()
new_hash = []
for word in ff.split():
    plain_text = word.encode()
    salt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(plain_text, salt)
    new_hash.append(hash_pass.decode('utf-8'))

f.close()
end = time.time()

result = open("hashes_generados_5.txt", "w")
for i in new_hash:
    result.write(i+'\n')
result.close()

total_time = (end - start)
if total_time<60:
    print("Operación terminada en: ", truncate(total_time, 2), " segundos.")
elif total_time>=60 and total_time<3600:
    print("Operación terminada en: ", truncate(total_time/60, 2), " minutos.")
else:
    print("Operación terminada en: ", truncate(total_time/3600, 2), " horas.")

