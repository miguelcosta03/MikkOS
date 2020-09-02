from site_connectivity_checker import site_connectivity_checker
from host_ip import host_ip
from port_scanner import port_scanner
from calculator import calculator
from ip_generator import ip_generator
from send_email import send_email
from internet_speed_tester import internet_speed_tester
from send_user_email import send_user_email
from user_email_sender import user_email_sender
from whats_my_ip import whats_my_ip
from time import sleep
from datetime import datetime

print('Welcome to MikkOs!')
print('---' * 40)

date = datetime.now()
sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

sys_log = open('logs.txt', "a")
sys_log.write(f"\n[{sys_date}] MikkOS Started \n")
sys_log.close()

print('Tools: '
      '\n[1] - Site Tools;'
      '\n[2] - Calculator;'
      '\n[3] - IPV4/IPV6 Generator;'
      '\n[4] - Internet Speed Tester'
      '\n[5] - Exit;')

print("Other commands: \nType 'vlog' to view your system program logs; "
      "\nType 'sysv' to see the version of Site Tools;"
      "\nType 'helpemail' to send an email to MikkOS support if there's something wrong with the MikkOS tools and logs "
      "or to get support from MikkOS Support Team;"
      "\nType 'sendemail' to send an email to the person you want;"
      "\nType 'myip' to check your IPv4 adress;")

tools = str(input("> Option: "))

if tools == '1':
    date = datetime.now()
    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
    sys_log = open("logs.txt", "a")
    sys_log.write(f"[{sys_date}] Site Tools selected.\n")
    sys_log.close()
    print()
    print('Entering in Site Tools...')

    print('Site Tools:'
          '\n[1] - Site Connectivity Checker;'
          '\n[2] - Host IP;'
          '\n[3] - Port Scanner;'
          '\n[4] - Exit;')
    site_tools = int(input('> Option: '))

    if site_tools == 1:
        site_connectivity_checker()
        print('---' * 40)

    elif site_tools == 2:
        host_ip()
        print('---' * 40)
    elif site_tools == 3:
        port_scanner()
        print('---' * 40)

    elif site_tools == 4:
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] MikkOS Quitted.\n")
        sys_log.close()
        print('Quitting MikkOS...')
        email = str(input('Can we send you an email with the logs?: [Y]-Yes / [N]- No: '))
        if email == 'Y':
            send_email()
        else:
            sleep(1)
        print('MikkOS Quitted.')
        sleep(1)

elif tools == '2':
    calculator()

elif tools == '3':
    ip_generator()

elif tools == '4':
    internet_speed_tester()

elif tools == '5':
    date = datetime.now()
    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
    sys_log = open("logs.txt", "a")
    sys_log.write(f"[{sys_date}] MikkOS Quitted.\n")
    sys_log.close()
    print('Quitting MikkOS')
    email = str(input('Can we send you an email with the logs?: [Y]-Yes / [N]- No: '))
    if email == 'Y':
        send_email()
    else:
        sleep(1)
    print('MikkOS Quitted.')

elif tools == 'vlog':
    logs = open("logs.txt", "r")
    print(logs.read())
    date = datetime.now()
    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
    sys_log = open("logs.txt", "a")
    sys_log.write(f"[{sys_date}] Checked user logs.\n")
    sys_log.close()

elif tools == 'sysv':
    print('MikkOS Version: 0.0.1')
    date = datetime.now()
    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
    sys_log = open("logs.txt", "a")
    sys_log.write(f"[{sys_date}] Checked the version of MikkOS. Version: 0.0.1\n")
    sys_log.close()

elif tools == 'helpemail':
    send_user_email()

elif tools == 'sendemail':
    user_email_sender()

elif tools == 'myip':
    whats_my_ip()

while tools != 5:
    print('Tools: '
          '\n[1] - Site Tools;'
          '\n[2] - Calculator;'
          '\n[3] - IPV4/IPV6 Generator;'
          '\n[4] - Internet Speed Tester;'
          '\n[5] - Exit;')

    print("Other commands: \nType 'vlog' to view your system program logs; "
          "\nType 'sysv' to see the version of Site Tools;"
          "\nType 'helpemail' to send an email to MikkOS support if there's something wrong with the MikkOS tools "
          "and logs or to get support from MikkOS Support Team;"
          "\nType 'sendemail' to send an email to the person you want;"
          "\nType 'myip' to check your IPv4 adress;")

    tools = str(input("> Option: "))

    if tools == '1':
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] Site Tools selected\n")
        sys_log.close()
        print()
        print('Entering in Site Tools...')
        print()
        print('Site Tools:'
              '\n[1] - Site Connectivity Checker;'
              '\n[2] - Host IP;'
              '\n[3] - Port Scanner;'
              '\n[4] - Exit;')

        site_tools = int(input('> Option: '))
        while site_tools != 4:
            if site_tools == 1:
                site_connectivity_checker()
                print('---' * 40)

            elif site_tools == 2:
                host_ip()
                print('---' * 40)
            elif site_tools == 3:
                port_scanner()
                print('---' * 40)

            elif site_tools == 4:
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] MikkOS Quitted\n")
                sys_log.close()
                print('Quitting MikkOS...')

                email = str(input('Can we send you an email with the logs?: [Y]-Yes / [N]- No: '))
                if email == 'Y':
                    send_email()
                else:
                    sleep(1)
                print('MikkOS Quitted.')
                break

    elif tools == '2':
        calculator()

    elif tools == '3':
        ip_generator()

    elif tools == '4':
        internet_speed_tester()

    elif tools == '5':
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] MikkOS Quitted\n")
        sys_log.close()
        email = str(input('Can we send you an email with the logs?: [Y]-Yes / [N]- No: '))
        if email == 'Y':
            send_email()
        else:
            sleep(1)
        print('MikkOS Quitted')
        break

    elif tools == 'vlog':
        logs = open("logs.txt", "r")
        print(logs.read())
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] Checked user logs\n")
        sys_log.close()

    elif tools == 'sysv':
        print('MikkOS Version: 0.0.1')
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] Checked the version of MikkOS. Version: 0.0.1\n")
        sys_log.close()

    elif tools == 'helpemail':
        send_user_email()

    elif tools == 'sendemail':
        user_email_sender()

    elif tools == 'myip':
        whats_my_ip()
