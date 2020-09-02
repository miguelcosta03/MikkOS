from time import sleep
from datetime import datetime
from random import randint, choice


def ip_generator():
    print('[1] - IP Generator;'
          '\n[2] - Exit')
    tool = int(input('> Option: '))
    if tool == 1:

        print('IP Generator Options: '
              '\n[1] - IPV4 Generator;'
              '\n[2] - IPV6 Generator;'
              '\n[3] - Exit;')

        ip_option = int(input('> Option: '))
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] Accessed IP Generator tool.\n")
        sys_log.close()

        if ip_option == 1:
            # IPV4 EXAMPLE: 123.456.789
            n1 = randint(100, 255)
            n2 = randint(100, 255)
            n3 = randint(100, 255)
            n4 = randint(1, 255)
            print(f'Random IPV4 generated: {n1}.{n2}.{n3}.{n4}')

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Generated an random IPV4: {n1}.{n2}.{n3}.{n4}\n")
            sys_log.close()

        if ip_option == 2:
            # IPV6 EXAMPLE: 1234:5AB7:CD89:FE01
            letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
            numbers = []
            for number in range(1, 10):
                n = randint(1, 9)
                numbers.append(n)

            char_list = letters_list + numbers
            ipv6_char_list = []
            while len(ipv6_char_list) < 50:
                rc = choice(char_list)
                ipv6_char_list.append(rc)

            n1 = randint(1000, 10000)
            n2 = ipv6_char_list[0:4]
            n3 = ipv6_char_list[5:9]
            n4 = ipv6_char_list[10:14]

            print('Random IPV6 Generated: ')
            print(f'{n1}:{n2}:{n3}::{n4}'.replace(',', '').replace(' ', '').replace("'", "").replace('[', '')
                  .replace(']', ''))
            print()

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f'[{sys_date}] Random IPV6 Generated: ')
            sys_log.write(f"[{n1}:{n2}:{n3}::{n4}\n".replace(',', '').replace(' ', '')
                          .replace("'", "").replace('[', '').replace(']', ''))
            sys_log.close()


        elif ip_option == 3:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] IP Generator Quitted.")
            sys_log.close()

            print('Quitting IP Generator...')
            sleep(1)
            print('IP Generator Quitted.')
    elif tool == 2:
        print('Quitting IP Generator...')
        sleep(1)
        print('IP Generator Quitted.')

        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

        sys_log = open("logs.txt", "a")
        sys_log.write(f"{sys_date} IP Generator Tool Quitted.")
        sys_log.close()

    while tool != 2:
        print('[1] - IP Generator;'
              '\n[2] - Exit')
        tool = int(input('> Option: '))
        if tool == 1:

            print('IP Generator Options: '
                  '\n[1] - IPV4 Generator;'
                  '\n[2] - IPV6 Generator;'
                  '\n[3] - Exit;')

            ip_option = int(input('> Option: '))
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Accessed IP Generator tool.\n")
            sys_log.close()

            if ip_option == 1:
                # IPV4 EXAMPLE: 123.456.789
                n1 = randint(100, 255)
                n2 = randint(100, 255)
                n3 = randint(100, 255)
                n4 = randint(1, 255)
                print(f'Random IPV4 generated: {n1}.{n2}.{n3}.{n4}')

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] Generated an random IPV4: {n1}.{n2}.{n3}.{n4}\n")
                sys_log.close()

            if ip_option == 2:
                # IPV6 EXAMPLE: 1234:5AB7:CD89:FE01
                letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
                numbers = []
                for number in range(1, 10):
                    n = randint(1, 9)
                    numbers.append(n)

                char_list = letters_list + numbers
                ipv6_char_list = []
                while len(ipv6_char_list) < 50:
                    rc = choice(char_list)
                    ipv6_char_list.append(rc)

                n1 = randint(1000, 10000)
                n2 = ipv6_char_list[0:4]
                n3 = ipv6_char_list[5:9]
                n4 = ipv6_char_list[10:14]

                print('Random IPV6 Generated: ')
                print(f'{n1}:{n2}:{n3}::{n4}'.replace(',', '').replace(' ', '').replace("'", "").replace('[', '')
                      .replace(']', ''))
                print()

                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f'[{sys_date}] Random IPV6 Generated: ')
                sys_log.write(f"[{n1}:{n2}:{n3}::{n4}\n".replace(',', '').replace(' ', '')
                              .replace("'", "").replace('[', '').replace(']', ''))
                sys_log.close()


            elif ip_option == 3:
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] IP Generator Quitted.")
                sys_log.close()

                print('Quitting IP Generator...')
                sleep(1)
                print('IP Generator Quitted.')
        elif tool == 2:
            print('Quitting IP Generator...')
            sleep(1)
            print('IP Generator Quitted.')

            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

            sys_log = open("logs.txt", "a")
            sys_log.write(f"{sys_date} IP Generator Tool Quitted.")
            sys_log.close()
            break
