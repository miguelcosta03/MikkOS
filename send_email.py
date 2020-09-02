import smtplib
from time import sleep
import socket
from datetime import datetime

logs = open("logs.txt", "r")


def send_email():
    host = '8.8.8.8'
    port = 53
    date = datetime.now()
    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
    sys_log = open("logs.txt", "a")
    sys_log.write(f"[{sys_date}] - Accessed Send Email Tool\n")
    sys_log.close()

    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Tried to establish a connection to the Internet\n")
        sys_log.close()

    except socket.error:
        print('MikkOS cannot establish an internet connection using this device. Please make sure your '
              'device is connected to the internet, and if the error persists please contact the '
              'MikkOS support team.')
        date = datetime.now()
        sys_date = str(date.strftime('%d-%m-%Y %H:%M:%S'))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - An error occurred while trying to connect to the internet\n")
        sys_log.close()

    else:
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Internet connection established successfully\n")
        sys_log.close()

        user_email = str(input('Enter your email so we can send you your logs: '))
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email, password)
        server.sendmail("mikkosofficial@gmail.com", user_email,
                        f"{logs.read()}")

        sleep(1)
        print(f'Email sent to {user_email}!')
        sleep(1)
        server.quit()
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Email sent to {user_email}\n.")
        sys_log.close()
