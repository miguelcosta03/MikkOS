import urllib
import urllib.request
import socket
from datetime import datetime


def site_connectivity_checker():
    print('[1] - Site Connectivity Checker;'
          '\n[2] - Exit;')
    tool = int(input('> Option: '))

    if tool == 1:
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] Site Connectivity Checker tool selected\n")
        sys_log.close()
        print()
        print('Entering in Site Connectivity Checker...')

        site_internet_checker_host = '8.8.8.8'
        site_internet_checker_port = 53

        try:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((site_internet_checker_host,
                                                                       site_internet_checker_port))

        except socket.error:
            print('{}MikkOS cannot establish an internet connection using this device. Please make sure your '
                  'device is connected to the internet, and if the error persists please contact the '
                  'MikkOS support team.')

        else:
            site_link = str(input('Site URL: '))
            if site_link[0] == 'h' and site_link[1] == 't' and site_link[2] == 't' and site_link[3] == 'p' and \
                    site_link[4] == 's':
                try:
                    site_connectivity = urllib.request.urlopen(site_link)
                except urllib.error.URLError:
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] Checked if the site {site_link} was online. Result: Site offline\n")
                    sys_log.close()
                    print(f'The site {site_link} is offline.')

                else:
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] Checked if the site {site_link} was online. Result: Site online\n")
                    sys_log.close()
                    print(f'The site {site_link} is online.')
            else:
                https = 'https://'
                try:
                    site_connectivity = urllib.request.urlopen(https + site_link)
                except urllib.error.URLError:
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(
                        f"[{sys_date}] Checked if the site {https + site_link} was online. Result: Site offline\n")
                    sys_log.close()
                    print(f'The site {https + site_link} is offline.')
                else:
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(
                        f"[{sys_date}] Checked if the site {https + site_link} was online. Result: Site online\n")
                    sys_log.close()
                    print(f'The site {https + site_link} is online.')
    if tool == 2:
        print('Quitting Site Connectivity Checker...')
        print('Site Connectivity Checker Quitted')

        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

        sys_log = open("logs.txt", "a")
        sys_log.write(f"{sys_date} Site Connectivity Checker Quitted.")
        sys_log.close()

    while tool != 2:
        print('[1] - Site Connectivity Checker;'
              '\n[2] - Exit;')
        tool = int(input('> Option: '))
        if tool == 1:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Site Connectivity Checker tool selected\n")
            sys_log.close()
            print()
            print('Entering in Site Connectivity Checker...')

            site_internet_checker_host = '8.8.8.8'
            site_internet_checker_port = 53

            try:
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((site_internet_checker_host,
                                                                           site_internet_checker_port))

            except socket.error:
                print('MikkOS cannot establish an internet connection using this device. Please make sure your '
                      'device is connected to the internet, and if the error persists please contact the '
                      'MikkOS support team')

            else:
                site_link = str(input('Site URL: '))
                if site_link[0] == 'h' and site_link[1] == 't' and site_link[2] == 't' and site_link[3] == 'p' and \
                        site_link[4] == 's':
                    try:
                        site_connectivity = urllib.request.urlopen(site_link)
                    except urllib.error.URLError:
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] Checked if the site {site_link} was online. Result: Site offline\n")
                        sys_log.close()
                        print(f'The site {site_link} is offline.')

                    else:
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] Checked if the site {site_link} was online. Result: Site online\n")
                        sys_log.close()
                        print(f'The site {site_link} is online.')
                else:
                    https = 'https://'
                    try:
                        site_connectivity = urllib.request.urlopen(https + site_link)
                    except urllib.error.URLError:
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(
                            f"[{sys_date}] Checked if the site {https + site_link} was online. Result: Site offline\n")
                        sys_log.close()
                        print(f'The site {https + site_link} is offline.')
                    else:
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(
                            f"[{sys_date}] Checked if the site {https + site_link} was online. Result: Site online\n")
                        sys_log.close()
                        print(f'The site {https + site_link} is online.')
        if tool == 2:
            print('Quitting Site Connectivity Checker...')
            print('Site Connectivity Checker Quitted')
            print()
            break
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

            sys_log = open("logs.txt", "a")
            sys_log.write(f"{sys_date} Site Connectivity Checker Quitted.\n")
            sys_log.close()
