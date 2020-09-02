import speedtest
from time import sleep
from datetime import datetime
import socket


def internet_speed_tester():
    host = '8.8.8.8'
    port = 53

    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

    except socket.error:
        print('MikkOS cannot establish an internet connection using this device. Please make sure your '
              'device is connected to the internet, and if the error persists please contact the '
              'MikkOS support team.')

    else:
        print('[1] - Internet Speed Tester;'
              '\n[2] - Exit;')
        tool = int(input('> Option: '))
        if tool == 1:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"\n[{sys_date}] - Acessed Speed Test tool\n")
            sys_log.close()
            test = speedtest.Speedtest()

            print('[1] - Test your Download Speed;'
                  '\n[2] - Test your Upload Speed;'
                  '\n[3] - Exit')
            option = int(input('> Option: '))
            if option == 1:
                date = datetime.now()
                test = speedtest.Speedtest()
                download = test.download()
                print(f"Download speed: {download}")

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Tested Internet Download Speed. Result: {download}\n")
                sys_log.close()

            elif option == 2:
                upload = test.upload()
                print(f"Upload speed: {upload}")

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Tested Internet Upload Speed. Result: {upload}\n")
                sys_log.close()

            elif option == 3:
                print('Quitting Speed Test...')
                sleep(1)
                print('Speed Test Quitted')

            while test != 3:
                test = speedtest.Speedtest()
                print('[1] - Test your Download Speed;'
                      '\n[2] - Test your Upload Speed;'
                      '\n[3] - Exit')
                option = int(input('> Option: '))

                if option == 1:
                    download = test.download()
                    print(f"Download speed: {download}")

                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - Tested Internet Download Speed. Result: {download}\n")

                elif option == 2:
                    upload = test.upload()
                    print(f"Upload speed: {upload}")
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - Tested Internet Upload Speed. Result: {upload}\n")

                elif option == 3:
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - Quitted Speed Test Tool\n")
                    sys_log.close()

                    print('Quitting Speed Test...')
                    sleep(1)
                    print('Speed Test Quitted')
                    break
        if tool == 2:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - Quitted Speed Test Tool\n")
            sys_log.close()

            print('Quitting Speed Test...')
            sleep(1)
            print('Speed Test Quitted')

        while tool != 2:
            print('[1] - Internet Speed Tester;'
                  '\n[2] - Exit;')
            tool = int(input('> Option: '))
            if tool == 1:
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Acessed Speed Test tool\n")
                sys_log.close()
                test = speedtest.Speedtest()

                print('[1] - Test your Download Speed;'
                      '\n[2] - Test your Upload Speed;'
                      '\n[3] - Exit')
                option = int(input('> Option: '))
                if option == 1:
                    date = datetime.now()
                    test = speedtest.Speedtest()
                    download = test.download()
                    print(f"Download speed: {download}")

                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - Tested Internet Download Speed. Result: {download}\n")
                    sys_log.close()

                elif option == 2:
                    upload = test.upload()
                    print(f"Upload speed: {upload}")

                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - Tested Internet Upload Speed. Result: {upload}\n")
                    sys_log.close()

                elif option == 3:
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - Quitted Speed Test Tool\n")
                    sys_log.close()

                    print('Quitting Speed Test...')
                    sleep(1)
                    print('Speed Test Quitted')

                while test != 3:
                    test = speedtest.Speedtest()
                    print('[1] - Test your Download Speed;'
                          '\n[2] - Test your Upload Speed;'
                          '\n[3] - Exit')
                    option = int(input('> Option: '))

                    if option == 1:
                        download = test.download()
                        print(f"Download speed: {download}")

                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] - Tested Internet Download Speed. Result: {download}\n")
                        sys_log.close()

                    elif option == 2:
                        upload = test.upload()
                        print(f"Upload speed: {upload}")
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] - Tested Internet Upload Speed. Result: {upload}\n")
                        sys_log.close()

                    elif option == 3:
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] - Quitted Speed Test Tool")
                        sys_log.close()

                        print('Quitting Speed Test...')
                        sleep(1)
                        print('Speed Test Quitted')
                        break
            if tool == 2:
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Quitted Speed Test Tool\n")
                sys_log.close()

                print('Quitting Speed Test...')
                sleep(1)
                print('Speed Test Quitted')
