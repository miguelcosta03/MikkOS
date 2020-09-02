from random import choice
import string
from time import sleep
from datetime import datetime


def password_generator():
    print('[1] - Random Password Generator;'
          '\n[2] - Exit; ')
    tool = int(input('> Option: '))

    if tool == 1:
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Random Password Tool selected.\n")
        sys_log.close()

        char_list = string.printable + string.ascii_uppercase + string.ascii_lowercase + "".join(
            str(i) for i in range(99))
        password = []
        num = ""

        for i in range(1, 100):
            num += str(i)

        while len(password) <= 10000:
            random_character = choice(char_list)
            password.append(random_character)

        password_char_number = int(input('How many characters should password have?'
                                         '(Maximum password Characters:1000): '))
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - User chose to form a random password of {password_char_number} characters\n")
        sys_log.close()

        formatted_password = str(password[0:password_char_number]).replace("[", "").replace("'", "") \
            .replace(",", "").replace("]", "").replace(" ", "")

        print(f'Your random password is: {formatted_password}')

        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Random Password Generated: {formatted_password}\n")
        sys_log.close()

    elif tool == 2:
        print('Quitting Random Password Tool...')
        sleep(1)
        print('Random Password Tool Quitted.')

        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Random Password Tool Quitted.\n")

    while tool != 2:
        print('[1] - Random Password Generator;'
              '\n[2] - Exit; ')
        tool = int(input('> Option: '))

        if tool == 1:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - Random Password Tool selected.\n")
            sys_log.close()

            char_list = string.printable + string.ascii_uppercase + string.ascii_lowercase + "".join(
                str(i) for i in range(99))
            password = []
            num = ""

            for i in range(1, 100):
                num += str(i)

            while len(password) <= 10000:
                random_character = choice(char_list)
                password.append(random_character)

            password_char_number = int(input('How many characters should password have?'
                                             '(Maximum password Characters:1000): '))
            formatted_password = str(password[0:password_char_number]).replace("[", "").replace("'", "") \
                .replace(",", "").replace("]", "").replace(" ", "")

            print(f'Your random password is: {formatted_password}')

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - User chose to form a random password of {password_char_number} "
                          f"characters.\n")
            sys_log.close()

        elif tool == 2:
            print('Quitting Random Password Tool...')
            sleep(1)
            print('Random Password Tool Quitted.')

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - Random Password Tool Quitted.\n")
