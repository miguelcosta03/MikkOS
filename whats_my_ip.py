from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider
from time import sleep
from datetime import datetime
import socket


def whats_my_ip():
    host = '8.8.8.8'
    port = 53
    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

    except socket.error:
        print('MikkOS cannot establish an internet connection using this device. Please make sure your '
              'device is connected to the internet, and if the error persists please contact the '
              'MikkOS support team.')

    else:
        print("[1] - What's My IP;"
              "\n[2] - Exit;")
        tool = int(input('> Option: '))

        if tool == 1:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - What's My IP tool selected.\n")
            sys_log.close()

            user_ip = get_ip(GoogleDnsProvider)
            print(f"Your IP is: {user_ip}")

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - User checked his IP. User IP: {user_ip}\n")
            sys_log.close()

        if tool == 2:
            print("Quitting What's My IP tool...")
            sleep(1)
            print("What's My IP tool Quitted. ")

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - What's My IP tool Quitted.\n")
            sys_log.close()

        while tool != 2:
            print("[1] - What's My IP;"
                  "\n[2] - Exit;")
            tool = int(input('> Option: '))

            if tool == 1:
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] What's My IP tool selected.\n")
                sys_log.close()

                user_ip = get_ip(GoogleDnsProvider)
                print(f"Your IP is: {user_ip}")

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - User checked his IP. User IP: {user_ip}\n")
                sys_log.close()

            if tool == 2:
                print("Quitting What's My IP tool...")
                sleep(1)
                print("What's My IP tool Quitted. ")

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - What's My IP tool Quitted.\n")
                sys_log.close()

