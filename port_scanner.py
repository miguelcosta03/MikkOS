import socket
from time import sleep
from datetime import datetime


def port_scanner():
    host = '8.8.8.8'
    port = 53
    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

    except socket.error:
        print('MikkOS cannot establish an internet connection using this device. Please make sure your '
              'device is connected to the internet, and if the error persists please contact the '
              'MikkOS support team.')

    else:
        print('[1] - Port Scanner;'
              '\n[2] - Exit')
        tool = int(input('> Option: '))
        if tool == 1:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Port Scanner tool selected\n")
            sys_log.close()
            print('Entering in Port Scanner...')
            sleep(3)

            host = str(input("Enter the server's ip: "))
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Entered a server ip: {host}\n")
            sys_log.close()

            port = int(input("Scanning Port: "))
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Entered a port number to scan: {port}\n")
            sys_log.close()


            def portScanner(port):
                try:
                    if s.connect((host, port)):
                        print(f'The port {port} is closed.')
                        scan_port = str(input(f'Do you want continue scanning any port of {host}?[Y]-Yes/[N]-No: '))
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] Port number {port} is closed\n")
                        sys_log.close()

                        while scan_port != 3:
                            if scan_port == 'Y':
                                print((f'Port Scanner Options:'
                                       f'\n[1] - Scan the same port (port{port});'
                                       f'\n[2] - Scan a different port;'
                                       f'\n[3] - Exit;'))
                                scan_port_options = int(input('> Option: '))

                                while scan_port_options != 3:
                                    if scan_port_options == 1:
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Selected the same port number to scan: Port{port}\n")
                                        sys_log.close()

                                        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        sk.settimeout(5)

                                        def port_Scanner(port):
                                            try:
                                                if sk.connect((host, port)):
                                                    print(f'The port {port} is closed.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                                f"Result: Port Closed.\n")
                                                    sys_log.close()
                                                else:
                                                    print(f'The port {port} is open.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                                  f"Result: Port Open.\n")
                                                    sys_log.close()

                                            except socket.timeout:
                                                print(f'The port {port} is closed.')
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                              f"Result: Port Closed.\n")
                                                sys_log.close()

                                        port_Scanner(port)

                                    elif scan_port_options == 2:
                                        new_port = int(input('Scanning port: '))
                                        sk_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        sk_connect.settimeout(5)

                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port number {new_port} of server {host} scanned.\n")
                                        sys_log.close()

                                        def port_Scanner(new_port):
                                            try:
                                                if sk_connect.connect((host, new_port)):
                                                    print(f'The port {new_port} is closed.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                                  f"Result: Port Closed.\n")
                                                    sys_log.close()
                                                else:
                                                    print(f'The port {new_port} is open.\n')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                                  f"Result: Port Open.\n")
                                                    sys_log.close()

                                            except socket.timeout:
                                                print(f'The port {new_port} is closed.')
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                              f"Result: Port Closed.\n")
                                                sys_log.close()

                                        port_Scanner(new_port)

                                    elif scan_port_options == 3:
                                        print('Port Scanner options:'
                                              '\n[1] Change the server ip for port scanner;'
                                              '\n[2] Exit')
                                        port_scanner_options = int(input('> Options: '))
                                        if port_scanner_options == 1:
                                            s_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s_connect.settimeout(5)

                                            new_host = str(input("Enter the server's ip: "))
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host}\n")
                                            sys_log.close()

                                            new_port = int(input("Scanning Port: "))
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(f"New port number for scan defined: Port number: {new_port}\n")
                                            sys_log.close()

                                            def port_Scanner(new_port):
                                                try:
                                                    if s_connect.connect((new_host, new_port)):
                                                        print(f'The port {new_port} is closed.')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                            f"Result: Port Closed.\n")
                                                        sys_log.close()
                                                    else:
                                                        print(f'The port {new_port} is open.')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                            f"Result: Port Open.\n")
                                                        sys_log.close()

                                                except socket.timeout:
                                                    print(f'The port {new_port} is closed.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                        f"Result: Port Closed.\n")
                                                    sys_log.close()


                                            port_Scanner(new_port)

                                        if port_scanner_options == 2:
                                            print('Quitting Port Scanner...')
                                            sleep(1)
                                            print('Port Scanner Quitted.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(f"[{sys_date}] Port Scan Quitted.\n")
                                            sys_log.close()

                            if scan_port == 'N':
                                print("Port Scanner options:"
                                      "\n[1] Change the server ip for port scanner;"
                                      "\n[2] Exit")
                                port_scanner_options = int(input('> Options: '))

                                if port_scanner_options == 1:
                                    socket_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                    socket_connect.settimeout(5)

                                    new_host = str(input("Enter the server's ip: "))
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host}\n")
                                    sys_log.close()

                                    new_port = int(input("Scanning Port: "))
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(f"[{sys_date}] New port number for scan defined: Port Number: {new_port}\n")
                                    sys_log.close()

                                    def port_Scanner(new_port):
                                        try:
                                            if socket_connect.connect((new_host, new_port)):
                                                print(f'The port {new_port} is closed.')
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                              f"Result: Port Closed.\n")
                                                sys_log.close()

                                            else:
                                                print(f'The port {new_port} is open.')
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                              f"Result: Port Open.\n")
                                                sys_log.close()

                                        except socket.timeout:
                                            print(f'The port {new_port} is closed.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                          f"Result: Port Closed.\n")
                                            sys_log.close()

                                    port_Scanner(new_port)

                                if port_scanner_options == 2:
                                    print('Quitting Port Scanner...')
                                    sleep(1)
                                    print('Port Scanner Quitted.')
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(f"[{sys_date}] Port Scanner Quitted.\n")
                                    sys_log.close()


                    else:
                        print(f'The port {port} is open')
                        continue_scanning = str(input(f'Do you want continue scanning {host} server ports?[Y]-Yes / [N]-No: '))
                        if continue_scanning == 'Y':
                            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s1.settimeout(5)

                            new_port = int(input("Scanning Port: "))
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] New port number for scan defined: Port: {new_port}\n")
                            sys_log.close()

                            def port_Scanner(new_port):
                                try:
                                    if s1.connect((host, new_port)):
                                        print(f'The port {new_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                      f"Result: Port Closed.\n")
                                        sys_log.close()
                                        print((f'Port Scanner Options:'
                                               f'\n[1] - Scan a different port;'
                                               f'\n[2] - Exit;'))
                                        scan_ports = int(input('> Option: '))
                                        while scan_ports != 3:
                                            if scan_ports == 1:
                                                sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                                sk1.settimeout(5)
                                                ip_host = str(input("Enter the server's ip: "))
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] New host IP defined: IP: {ip_host}\n")
                                                sys_log.close()

                                                new_server_port = int(input('Scanning Port: '))
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] New port for scan defined: Port: {new_server_port}\n")
                                                sys_log.close()

                                                def host_port_scan(new_server_port):
                                                    try:
                                                        if sk1.connect((ip_host, new_server_port)):
                                                            print(f'The port {new_host_port} is closed.')
                                                            date = datetime.now()
                                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                            sys_log = open("logs.txt", "a")
                                                            sys_log.write(f"[{sys_date}] Port number {new_server_port} of server {ip_host} scanned. "
                                                                f"Result: Port Closed.\n")
                                                            sys_log.close()
                                                        else:
                                                            print(f'The port {new_host_port} is open.\n')
                                                            date = datetime.now()
                                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                            sys_log = open("logs.txt", "a")
                                                            sys_log.write(f"[{sys_date}] Port number {new_server_port} of server {ip_host} scanned. "
                                                                f"Result: Port Open.\n")
                                                            sys_log.close()
                                                    except socket.timeout:
                                                        print(f'The port {new_host_port} is closed.')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(f"[{sys_date}] Port number {new_server_port} of server {ip_host} scanned. "
                                                            f"Result: Port Closed.\n")
                                                        sys_log.close()

                                                host_port_scan(new_server_port)
                                    else:
                                        print(f'The port {new_port} is open.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(
                                            f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                            f"Result: Port Open.\n")
                                        sys_log.close()
                                except socket.timeout:
                                    print(f'The port {new_port} is closed.')
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(
                                        f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                        f"Result: Port Closed.\n")
                                    sys_log.close()

                            port_Scanner(new_port)

                except socket.timeout:
                    print('The Port is closed-...')
                    print('Port Scanner options:'
                          '\n[1] Change the server ip for port scanner;'
                          '\n[2] Exit;')
                    new_port_scanner_options = int(input('> Options: '))

                    while new_port_scanner_options != 2:
                        if new_port_scanner_options == 1:

                            st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            st.settimeout(5)

                            new_host_ip = str(input("Enter the server's ip: "))
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host_ip}\n")
                            sys_log.close()

                            new_host_port = int(input("Scanning Port: "))
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] New port number for scan defined: Port: {new_host_port}\n")
                            sys_log.close()

                            def Port_Scanner(new_host_port):
                                try:
                                    if st.connect((new_host_ip, new_host_port)):
                                        print(f'The port {new_host_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port number {new_host_port} of server {new_host_ip} scanned. "
                                            f"Result: Port Closed.\n")
                                        sys_log.close()

                                    else:
                                        print(f'The port {new_host_port} is open.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(
                                            f"[{sys_date}] Port number {new_host_port} of server {new_host_ip} scanned. "
                                            f"Result: Port Open.\n")
                                        sys_log.close()

                                except socket.timeout:
                                    print(f'The port {new_host_port} is closed.')
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(f"[{sys_date}] Port number {new_host_port} of server {new_host_ip} scanned. "
                                                  f"Result: Port Closed.\n")
                                    sys_log.close()

                            Port_Scanner(new_host_port)

                        if new_port_scanner_options == 2:
                            print('Quitting Port Scanner...')
                            sleep(1)
                            print('Port Scanner Quitted.')
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] Port Scanner Quitted\n")
                            sys_log.close()
                            break

                else:
                    print(f"[1] - Scan another {host} server's port;"
                          "\n[2] - Change the server's IP for port scanner;"
                          "\n[3] - Exit;")

                    scan_port_op = int(input('> Option: '))
                    while scan_port_op != 3:
                        if scan_port_op == 1:
                            socket1_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            socket1_connect.settimeout(5)
                            new_scan_port = int(input('Scanning Port: '))
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] Port number {new_scan_port} of server {host} scanned.\n")
                            sys_log.close()

                            def new_port_scanner(new_scan_port):
                                try:
                                    if socket1_connect.connect((host, new_scan_port)):
                                        print(f'The port {new_scan_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port number {new_scan_port} of server {host} scanned. "
                                            f"Result: Port Closed.\n")
                                        sys_log.close()

                                    else:
                                        print(f'The port {new_scan_port} is open.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port number {new_scan_port} of server {host} scanned. "
                                                      f"Result: Port Open.\n")
                                        sys_log.close()

                                except socket.timeout:
                                    print(f'The port {new_scan_port} is closed.')
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(f"[{sys_date}] Port number {new_scan_port} of server {host} scanned. "
                                                  f"Result: Port Closed.\n")
                                    sys_log.close()

                            new_port_scanner(new_scan_port)

                        if scan_port_op == 2:
                            socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            socket1.settimeout(5)

                            new_host_ip = str(input("Enter the server's ip: "))
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host_ip}\n")
                            sys_log.close()

                            new_scan_server_port = int(input('Scanning Port: '))
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] New port for scan defined: Port: {new_scan_server_port}\n")
                            sys_log.close()

                            def port_scan_server(new_scan_server_port):
                                try:
                                    if socket1.connect((new_host_ip, new_scan_server_port)):
                                        print(f'The port {new_scan_server_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port number {new_scan_server_port} of server {new_host_ip} scanned. "
                                                      f"Result: Port Closed.\n")
                                        sys_log.close()

                                    else:
                                        print(f'The port {new_scan_server_port} is open.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(
                                            f"[{sys_date}] Port number {new_scan_server_port} of server {new_host_ip} scanned. "
                                            f"Result: Port Open.\n")
                                        sys_log.close()

                                except socket.timeout:
                                    print(f'The port {new_scan_server_port} is closed.')
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(
                                        f"[{sys_date}] Port number {new_scan_server_port} of server {new_host_ip} scanned. "
                                        f"Result: Port Closed.\n")
                                    sys_log.close()

                            port_scan_server(new_scan_server_port)

                    if scan_port_op == 3:
                        print('Quitting Port Scanner...')
                        sleep(1)
                        print('Port Scanner Quitted.')
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] Port Scanner Quitted\n")
                        sys_log.close()

            portScanner(port)

        elif tool == 2:
            print('Quitting Port Scanner...')
            sleep(1)
            print('Port Scanner Quitted.')

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Port Scanner Quitted.")

        while tool != 2:
            print('[1] - Port Scanner;'
                  '\n[2] - Exit')
            tool = int(input('> Option: '))
            if tool == 1:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] Port Scanner tool selected\n")
                sys_log.close()
                print('Entering in Port Scanner...')
                sleep(3)

                host = str(input("Enter the server's ip: "))
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] Entered a server ip: {host}\n")
                sys_log.close()

                port = int(input("Scanning Port: "))
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] Entered a port number to scan: {port}\n")
                sys_log.close()

                def portScanner(port):
                    try:
                        if s.connect((host, port)):
                            print(f'The port {port} is closed.')
                            scan_port = str(input(f'Do you want continue scanning any port of {host}?[Y]-Yes/[N]-No: '))
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] Port number {port} is closed\n")
                            sys_log.close()

                            while scan_port != 3:
                                if scan_port == 'Y':
                                    print((f'Port Scanner Options:'
                                           f'\n[1] - Scan the same port (port{port});'
                                           f'\n[2] - Scan a different port;'
                                           f'\n[3] - Exit;'))
                                    scan_port_options = int(input('> Option: '))

                                    while scan_port_options != 3:
                                        if scan_port_options == 1:
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Selected the same port number to scan: Port{port}\n")
                                            sys_log.close()

                                            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            sk.settimeout(5)

                                            def port_Scanner(port):
                                                try:
                                                    if sk.connect((host, port)):
                                                        print(f'The port {port} is closed.')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(
                                                            f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                            f"Result: Port Closed.\n")
                                                        sys_log.close()
                                                    else:
                                                        print(f'The port {port} is open.')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(
                                                            f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                            f"Result: Port Open.\n")
                                                        sys_log.close()

                                                except socket.timeout:
                                                    print(f'The port {port} is closed.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(
                                                        f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                        f"Result: Port Closed.\n")
                                                    sys_log.close()

                                            port_Scanner(port)

                                        elif scan_port_options == 2:
                                            new_port = int(input('Scanning port: '))
                                            sk_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            sk_connect.settimeout(5)

                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_port} of server {host} scanned.\n")
                                            sys_log.close()

                                            def port_Scanner(new_port):
                                                try:
                                                    if sk_connect.connect((host, new_port)):
                                                        print(f'The port {new_port} is closed.')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(
                                                            f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                            f"Result: Port Closed.\n")
                                                        sys_log.close()
                                                    else:
                                                        print(f'The port {new_port} is open.\n')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(
                                                            f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                            f"Result: Port Open.\n")
                                                        sys_log.close()

                                                except socket.timeout:
                                                    print(f'The port {new_port} is closed.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(
                                                        f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                        f"Result: Port Closed.\n")
                                                    sys_log.close()

                                            port_Scanner(new_port)

                                        elif scan_port_options == 3:
                                            print('Port Scanner options:'
                                                  '\n[1] Change the server ip for port scanner;'
                                                  '\n[2] Exit')
                                            port_scanner_options = int(input('> Options: '))
                                            if port_scanner_options == 1:
                                                s_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                                s_connect.settimeout(5)

                                                new_host = str(input("Enter the server's ip: "))
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host}\n")
                                                sys_log.close()

                                                new_port = int(input("Scanning Port: "))
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(
                                                    f"New port number for scan defined: Port number: {new_port}\n")
                                                sys_log.close()

                                                def port_Scanner(new_port):
                                                    try:
                                                        if s_connect.connect((new_host, new_port)):
                                                            print(f'The port {new_port} is closed.')
                                                            date = datetime.now()
                                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                            sys_log = open("logs.txt", "a")
                                                            sys_log.write(
                                                                f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                                f"Result: Port Closed.\n")
                                                            sys_log.close()
                                                        else:
                                                            print(f'The port {new_port} is open.')
                                                            date = datetime.now()
                                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                            sys_log = open("logs.txt", "a")
                                                            sys_log.write(
                                                                f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                                f"Result: Port Open.\n")
                                                            sys_log.close()

                                                    except socket.timeout:
                                                        print(f'The port {new_port} is closed.')
                                                        date = datetime.now()
                                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                        sys_log = open("logs.txt", "a")
                                                        sys_log.write(
                                                            f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                            f"Result: Port Closed.\n")
                                                        sys_log.close()

                                                port_Scanner(new_port)

                                            if port_scanner_options == 2:
                                                print('Quitting Port Scanner...')
                                                sleep(1)
                                                print('Port Scanner Quitted.')
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(f"[{sys_date}] Port Scan Quitted.\n")
                                                sys_log.close()

                                if scan_port == 'N':
                                    print("Port Scanner options:"
                                          "\n[1] Change the server ip for port scanner;"
                                          "\n[2] Exit")
                                    port_scanner_options = int(input('> Options: '))

                                    if port_scanner_options == 1:
                                        socket_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        socket_connect.settimeout(5)

                                        new_host = str(input("Enter the server's ip: "))
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host}\n")
                                        sys_log.close()

                                        new_port = int(input("Scanning Port: "))
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(
                                            f"[{sys_date}] New port number for scan defined: Port Number: {new_port}\n")
                                        sys_log.close()

                                        def port_Scanner(new_port):
                                            try:
                                                if socket_connect.connect((new_host, new_port)):
                                                    print(f'The port {new_port} is closed.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(
                                                        f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                        f"Result: Port Closed.\n")
                                                    sys_log.close()

                                                else:
                                                    print(f'The port {new_port} is open.')
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(
                                                        f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                        f"Result: Port Open.\n")
                                                    sys_log.close()

                                            except socket.timeout:
                                                print(f'The port {new_port} is closed.')
                                                date = datetime.now()
                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                sys_log = open("logs.txt", "a")
                                                sys_log.write(
                                                    f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                    f"Result: Port Closed.\n")
                                                sys_log.close()

                                        port_Scanner(new_port)

                                    if port_scanner_options == 2:
                                        print('Quitting Port Scanner...')
                                        sleep(1)
                                        print('Port Scanner Quitted.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port Scanner Quitted.\n")
                                        sys_log.close()


                        else:
                            print(f'The port {port} is open')
                            continue_scanning = str(
                                input(f'Do you want continue scanning {host} server ports?[Y]-Yes / [N]-No: '))
                            if continue_scanning == 'Y':
                                s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s1.settimeout(5)

                                new_port = int(input("Scanning Port: "))
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] New port number for scan defined: Port: {new_port}\n")
                                sys_log.close()

                                def port_Scanner(new_port):
                                    try:
                                        if s1.connect((host, new_port)):
                                            print(f'The port {new_port} is closed.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_port} of server {new_host} scanned. "
                                                f"Result: Port Closed.\n")
                                            sys_log.close()
                                            print((f'Port Scanner Options:'
                                                   f'\n[1] - Scan a different port;'
                                                   f'\n[2] - Exit;'))
                                            scan_ports = int(input('> Option: '))
                                            while scan_ports != 3:
                                                if scan_ports == 1:
                                                    sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                                    sk1.settimeout(5)
                                                    ip_host = str(input("Enter the server's ip: "))
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(f"[{sys_date}] New host IP defined: IP: {ip_host}\n")
                                                    sys_log.close()

                                                    new_server_port = int(input('Scanning Port: '))
                                                    date = datetime.now()
                                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                    sys_log = open("logs.txt", "a")
                                                    sys_log.write(
                                                        f"[{sys_date}] New port for scan defined: Port: {new_server_port}\n")
                                                    sys_log.close()

                                                    def host_port_scan(new_server_port):
                                                        try:
                                                            if sk1.connect((ip_host, new_server_port)):
                                                                print(f'The port {new_host_port} is closed.')
                                                                date = datetime.now()
                                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                                sys_log = open("logs.txt", "a")
                                                                sys_log.write(
                                                                    f"[{sys_date}] Port number {new_server_port} of server {ip_host} scanned. "
                                                                    f"Result: Port Closed.\n")
                                                                sys_log.close()
                                                            else:
                                                                print(f'The port {new_host_port} is open.\n')
                                                                date = datetime.now()
                                                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                                sys_log = open("logs.txt", "a")
                                                                sys_log.write(
                                                                    f"[{sys_date}] Port number {new_server_port} of server {ip_host} scanned. "
                                                                    f"Result: Port Open.\n")
                                                                sys_log.close()
                                                        except socket.timeout:
                                                            print(f'The port {new_host_port} is closed.')
                                                            date = datetime.now()
                                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                                            sys_log = open("logs.txt", "a")
                                                            sys_log.write(
                                                                f"[{sys_date}] Port number {new_server_port} of server {ip_host} scanned. "
                                                                f"Result: Port Closed.\n")
                                                            sys_log.close()

                                                    host_port_scan(new_server_port)
                                        else:
                                            print(f'The port {new_port} is open.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                                f"Result: Port Open.\n")
                                            sys_log.close()
                                    except socket.timeout:
                                        print(f'The port {new_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(
                                            f"[{sys_date}] Port number {new_port} of server {host} scanned. "
                                            f"Result: Port Closed.\n")
                                        sys_log.close()

                                port_Scanner(new_port)

                    except socket.timeout:
                        print('The Port is closed-...')
                        print('Port Scanner options:'
                              '\n[1] Change the server ip for port scanner;'
                              '\n[2] Exit;')
                        new_port_scanner_options = int(input('> Options: '))

                        while new_port_scanner_options != 2:
                            if new_port_scanner_options == 1:

                                st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                st.settimeout(5)

                                new_host_ip = str(input("Enter the server's ip: "))
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host_ip}\n")
                                sys_log.close()

                                new_host_port = int(input("Scanning Port: "))
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] New port number for scan defined: Port: {new_host_port}\n")
                                sys_log.close()

                                def Port_Scanner(new_host_port):
                                    try:
                                        if st.connect((new_host_ip, new_host_port)):
                                            print(f'The port {new_host_port} is closed.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_host_port} of server {new_host_ip} scanned. "
                                                f"Result: Port Closed.\n")
                                            sys_log.close()

                                        else:
                                            print(f'The port {new_host_port} is open.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_host_port} of server {new_host_ip} scanned. "
                                                f"Result: Port Open.\n")
                                            sys_log.close()

                                    except socket.timeout:
                                        print(f'The port {new_host_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(
                                            f"[{sys_date}] Port number {new_host_port} of server {new_host_ip} scanned. "
                                            f"Result: Port Closed.\n")
                                        sys_log.close()

                                Port_Scanner(new_host_port)

                            if new_port_scanner_options == 2:
                                print('Quitting Port Scanner...')
                                sleep(1)
                                print('Port Scanner Quitted.')
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] Port Scanner Quitted\n")
                                sys_log.close()
                                break

                    else:
                        print(f"[1] - Scan another {host} server's port;"
                              "\n[2] - Change the server's IP for port scanner;"
                              "\n[3] - Exit;")

                        scan_port_op = int(input('> Option: '))
                        while scan_port_op != 3:
                            if scan_port_op == 1:
                                socket1_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                socket1_connect.settimeout(5)
                                new_scan_port = int(input('Scanning Port: '))
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] Port number {new_scan_port} of server {host} scanned.\n")
                                sys_log.close()

                                def new_port_scanner(new_scan_port):
                                    try:
                                        if socket1_connect.connect((host, new_scan_port)):
                                            print(f'The port {new_scan_port} is closed.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_scan_port} of server {host} scanned. "
                                                f"Result: Port Closed.\n")
                                            sys_log.close()

                                        else:
                                            print(f'The port {new_scan_port} is open.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_scan_port} of server {host} scanned. "
                                                f"Result: Port Open.\n")
                                            sys_log.close()

                                    except socket.timeout:
                                        print(f'The port {new_scan_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] Port number {new_scan_port} of server {host} scanned. "
                                                      f"Result: Port Closed.\n")
                                        sys_log.close()

                                new_port_scanner(new_scan_port)

                            if scan_port_op == 2:
                                socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                socket1.settimeout(5)

                                new_host_ip = str(input("Enter the server's ip: "))
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] New host IP defined: IP: {new_host_ip}\n")
                                sys_log.close()

                                new_scan_server_port = int(input('Scanning Port: '))
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] New port for scan defined: Port: {new_scan_server_port}\n")
                                sys_log.close()

                                def port_scan_server(new_scan_server_port):
                                    try:
                                        if socket1.connect((new_host_ip, new_scan_server_port)):
                                            print(f'The port {new_scan_server_port} is closed.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_scan_server_port} of server {new_host_ip} scanned. "
                                                f"Result: Port Closed.\n")
                                            sys_log.close()

                                        else:
                                            print(f'The port {new_scan_server_port} is open.')
                                            date = datetime.now()
                                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                            sys_log = open("logs.txt", "a")
                                            sys_log.write(
                                                f"[{sys_date}] Port number {new_scan_server_port} of server {new_host_ip} scanned. "
                                                f"Result: Port Open.\n")
                                            sys_log.close()

                                    except socket.timeout:
                                        print(f'The port {new_scan_server_port} is closed.')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(
                                            f"[{sys_date}] Port number {new_scan_server_port} of server {new_host_ip} scanned. "
                                            f"Result: Port Closed.\n")
                                        sys_log.close()

                                port_scan_server(new_scan_server_port)

                        if scan_port_op == 3:
                            print('Quitting Port Scanner...')
                            sleep(1)
                            print('Port Scanner Quitted.')
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] Port Scanner Quitted\n")
                            sys_log.close()

                portScanner(port)

            elif tool == 2:
                print('Quitting Port Scanner...')
                sleep(1)
                print('Port Scanner Quitted.')

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] Port Scanner Quitted.")
                sys_log.close()
                break
