import time
import sys
import imaplib
import smtplib
import getpass
import email
import email.header
import datetime
import getpass
import re
import email
from email.header import Header, decode_header, make_header
from email.parser import Parser, HeaderParser
import calendar

EMAIL_ACCOUNT = ""
PW = ""
EMAIL_FOLDER = "INBOX"
SUBJECT = ""
FROM_ADDRESS = ''
MSG_ID = ""
MSG_IDS = []
DATE = ""
REGEX = ""


def process_mailbox(M):
    # try to log in to the mail server with your credentials
    try:
        rv, data = M.login(EMAIL_ACCOUNT, PW)
        print(rv, data)
    except imaplib.IMAP4.error:  # except an error and exit
        print("LOGIN FALLIDO!")
        sys.exit(1)

    # set the mail server for reading mails
    rv, data = M.select(EMAIL_FOLDER)

    if data == [b'']:
        print("El buzón esta vacio")
        return
    else:
        print(rv, data)
        rv, data = M.search(None, 'FROM', SUBJECT)

    # !!-----------------------------------------------------
    # here rv always return "OK" therefore the next if clause
    # also is always false although it should be True

    if rv != 'OK':
        print("No se encontraron mensajes en ", datetime.datetime.now())
        return

    i = 0
    parser = HeaderParser()
    global MSG_IDS
    MSG_IDS = []
    for num in data[0].split():
        if i < 40:
            rv, data = Mailbox.fetch(num, '(BODY[HEADER])')
            if rv != 'OK':
                print("ERROR obteniendo mensaje ", num)
                continue
            content = parser.parsestr(data[0][1].decode("utf-8"))
            if i == 0:
                global DATE
                global FROM_ADDRESS
                FROM_ADDRESS = content['From']
                f = FROM_ADDRESS.split(" ")
                FROM_ADDRESS = f[1]
                FROM_ADDRESS = FROM_ADDRESS.replace('<', '')
                FROM_ADDRESS = FROM_ADDRESS.replace('>', '')
                DATE = content['Date']
                j = 0
                dd = ""
                mm = ""
                aa = ""
                for words in DATE.split(" "):
                    if j == 1:
                        dd = str(words)
                        dd = dd.zfill(2)
                    elif j == 2:
                        mm = str(list(calendar.month_abbr).index(words))
                        mm = mm.zfill(2)
                    elif j == 3:
                        aa = str(words)
                        aa = aa.zfill(2)
                    j = j + 1
                DATE = f"{dd}/{mm}/{aa}"
                i = i + 1

            # returns tuple fetch(message_set, message parts)
            #rv, data = Mailbox.fetch(num, '(RFC822)')
            # if rv (assigned above) is OK print an error message and return
            global MSG_ID
            MSG_ID = content['Message-id']
            MSG_ID = MSG_ID.replace('<', '')
            MSG_ID = MSG_ID.replace('>', '')
            MSG_IDS.append(MSG_ID)

            #print(FROM_ADDRESS, DATE, MSG_ID)
            #msg = email.message_from_bytes(data[0][1])
            # decode the header and make a readable header
            # hdr = email.header.make_header(
            #    email.header.decode_header(msg['Subject']))
            # subject = str(hdr)  # convert the header to a string

            #print(subject, "\n------------\n")
        else:
            break

    Mailbox.close()
    Mailbox.logout()


def mailbox_match_search(M, Email, Regex):
    # try to log in to the mail server with your credentials
    try:
        rv, data = M.login(EMAIL_ACCOUNT, PW)
        print(rv, data)
    except imaplib.IMAP4.error:  # except an error and exit
        print("LOGIN FALLIDO!")
        sys.exit(1)

    # set the mail server for reading mails
    rv, data = M.select(EMAIL_FOLDER)

    if data == [b'']:
        print("El buzón esta vacio")
        return
    else:
        print(rv, data)
        dirr = f'From {Email}'
        rv, data = M.search(None, dirr)

    # !!-----------------------------------------------------
    # here rv always return "OK" therefore the next if clause
    # also is always false although it should be True

    if rv != 'OK':
        print("No se encontraron mensajes en ", datetime.datetime.now())
        return

    i = 0
    err = 0
    oldest = ""
    parser = HeaderParser()
    global MSG_IDS
    MSG_IDS = []
    for num in data[0].split():
        if i < 40:
            rv, data = Mailbox.fetch(num, '(BODY[HEADER])')
            if rv != 'OK':
                print("ERROR obteniendo mensaje ", num)
                continue
            content = parser.parsestr(data[0][1].decode("utf-8"))
            if i == 0:
                global DATE
                global FROM_ADDRESS
                FROM_ADDRESS = content['From']
                f = FROM_ADDRESS.split(" ")
                FROM_ADDRESS = f[1]
                FROM_ADDRESS = FROM_ADDRESS.replace('<', '')
                FROM_ADDRESS = FROM_ADDRESS.replace('>', '')
                DATE = content['Date']
                j = 0
                dd = ""
                mm = ""
                aa = ""
                for words in DATE.split(" "):
                    if j == 1:
                        dd = str(words)
                        dd = dd.zfill(2)
                    elif j == 2:
                        mm = str(list(calendar.month_abbr).index(words))
                        mm = mm.zfill(2)
                    elif j == 3:
                        aa = str(words)
                        aa = aa.zfill(2)
                    j = j + 1
                DATE = f"{dd}/{mm}/{aa}"
                i = i + 1

            # returns tuple fetch(message_set, message parts)
            #rv, data = Mailbox.fetch(num, '(RFC822)')
            # if rv (assigned above) is OK print an error message and return
            global MSG_ID
            MSG_ID = content['Message-id']
            MSG_ID = MSG_ID.replace('<', '')
            MSG_ID = MSG_ID.replace('>', '')
            MSG_IDS.append(MSG_ID)
            actual_date = content['Date']
            j = 0
            dd = ""
            mm = ""
            aa = ""
            for words in actual_date.split(" "):
                if j == 1:
                    if words == "":
                        j = 0
                    else:
                        dd = str(words)
                        dd = dd.zfill(2)
                elif j == 2:
                    mm = str(list(calendar.month_abbr).index(words))
                    mm = mm.zfill(2)
                elif j == 3:
                    aa = str(words)
                    aa = aa.zfill(2)
                elif j == 2:
                    mm = str(list(calendar.month_abbr).index(words))
                    mm = mm.zfill(2)
                elif j == 3:
                    aa = str(words)
                    aa = aa.zfill(2)
                j = j + 1
            actual_date = f"{dd}/{mm}/{aa}"
            mat = re.match(Regex, MSG_ID)
            if not mat:
                print("Se encontró un correo falso, con fecha:",
                      actual_date, "y message-id:", MSG_ID, "\n")
                if err == 0:
                    oldest = actual_date
                err = err + 1

            #print(FROM_ADDRESS, DATE, MSG_ID)
            #msg = email.message_from_bytes(data[0][1])
            # decode the header and make a readable header
            # hdr = email.header.make_header(
            #    email.header.decode_header(msg['Subject']))
            # subject = str(hdr)  # convert the header to a string

            #print(subject, "\n------------\n")
        else:
            break
    if err == 0:
        print("No se encontró ningún correo falso :D")
    else:
        print(
            f"\nSe encontraron {err} correos falsos. El correo falso mas antiguo tiene fecha {oldest}")
    Mailbox.close()
    Mailbox.logout()


option = 0
while True:
    print("-----------------------------------")
    print("Seleccione una operación: \n1.Buscar correos. \n2.Analizar dirección de correo con regex. \n9.Salir.\n-----------------------------------\n")
    option = int(input())
    if (option == 1):
        print("Ingrese su correo electronico: ")
        EMAIL_ACCOUNT = input()
        print("Ingrese su contraseña: ")
        PW = getpass.getpass()
        print("Ingrese el asunto para buscar los correos: ")
        SUBJECT = input()
        print("Procesando bandeja de entrada...\n")
        Mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
        process_mailbox(Mailbox)
        time.sleep(1)
        ids = len(MSG_IDS)
        while True:
            print("\nSe recolectaron", ids,
                  "message-id.¿Desea verlos?\n1.Si\n2.No")
            option2 = int(input())
            if option2 == 1:
                i = 0
                for words in MSG_IDS:
                    i = i + 1
                    print(i, ":", words)
                print("\nSe añadirá el correo '", FROM_ADDRESS, "' y la fecha del correo más antiguo (", DATE,
                      ")  al archivo register.txt. \nRecuerde añadir la expresión regular entre los ; ;\n\n---------------Fin-----------------")
                data = FROM_ADDRESS + ";[Inserte aqui la regex];" + DATE
                f = open("register.txt", "a")
                f.write(data + "\n")
                f.close()
                break
            elif option2 == 2:
                print("Se añadirá el correo '", FROM_ADDRESS, "' y la fecha del correo más antiguo (", DATE,
                      ")  al archivo register.txt. \nRecuerde añadir la expresión regular entre los ; ;\n\n---------------Fin-----------------")
                data = FROM_ADDRESS + ";[Inserte aqui la regex];" + DATE
                f = open("register.txt", "a")
                f.write(data + "\n")
                f.close()
                break
            else:
                print("Opción invalida, intente nuevamente.")

    elif (option == 2):
        print(
            "**Se buscará por el archivo 'register.txt' (formato: direccion;regex;fecha).**\n")
        try:
            f = open("./register.txt", "r")
            ff = f.read()
            email = []
            date = []
            regex = []
            for words in ff.split('\n'):
                i = 0
                for word in words.split(';'):
                    if i == 0:
                        email.append(word)
                        i = i + 1
                    elif i == 1:
                        regex.append(word)
                        i = i + 1
                    elif i == 2:
                        date.append(word)
                        i = i + 1
            f.close()
            i = 1
            print("Elija un correo a analizar (si el correo que busca no se encuentra en la lista,\npruebe volver al menú principal y pruebe la primera opción):\n")
            for words in email:
                if words == "":
                    break
                else:
                    print(i, "<", words, ">")
                    i = i + 1
            print("\n0 Volver al menú principal.\n")
            option3 = int(input())
            if option3 == 0:
                continue
            else:
                option3 = option3 - 1
                try:
                    print("Ingrese su correo electronico: ")
                    EMAIL_ACCOUNT = input()
                    print("Ingrese su contraseña: ")
                    PW = getpass.getpass()
                    Mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
                    mailbox_match_search(
                        Mailbox, email[option3], regex[option3])
                    break
                except IndexError:
                    print("Opción incorrecta, volviendo al menú principal...\n")
        except IOError:
            print("\nNo existe archivo 'register.txt'\n")
    elif (option == 9):
        break
    else:
        print("\nOpción incorrecta, intente nuevamente.\n")
