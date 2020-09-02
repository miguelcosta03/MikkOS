import socket
from time import sleep
from datetime import datetime


def host_ip():
    host = '8.8.8.8'
    port = 53
    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

    except socket.error:
        print('MikkOS cannot establish an internet connection using this device. Please make sure your '
              'device is connected to the internet, and if the error persists please contact the '
              'MikkOS support team.')

    else:
        print('[1] - Host IP;'
              '\n[2] - Exit;')

        tool = int(input('> Option: '))

        if tool == 1:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

            sys_log = open("logs.txt", "a")
            sys_log.write(f"\n[{sys_date}] Host IP tool selected.\n")
            sys_log.close()

            host = str(input('Site URL: '))
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Checked the server IP of {host}.\n")
            sys_log.close()

            print(f'The host ip of {host} is: {socket.gethostbyname(host)}')
        if tool == 2:
            print('Quitting Host IP...')
            sleep(1)
            print('Host IP Quitted')

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Host IP Tool Quitted")
            sys_log.close()

        while tool != 2:
            host = '8.8.8.8'
            port = 53
            print('[1] - Host IP;'
                  '\n[2] - Exit;')
            tool = int(input('> Option: '))
            if tool == 1:
                try:
                    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
                except socket.error:
                    print('MikkOS cannot establish an internet connection using this device. Please make sure your '
                          'device is connected to the internet, and if the error persists please contact the '
                          'MikkOS support team.')
                else:
                    print(f'The host ip of {host} is: {socket.gethostbyname(host)}')
                    host = str(input('Site URL: '))
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] Checked the server IP of {host}.\n")
                    sys_log.close()

            if tool == 2:
                print('Quitting Host IP...')
                sleep(1)
                print('Host IP Quitted')

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] Host IP Tool Quitted")
                sys_log.close()
                break