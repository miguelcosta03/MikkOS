from time import sleep
from datetime import datetime


def calculator():
    print('[1] - Calculator;'
          '\n[2] - Exit')
    tool = int(input('> Option: '))
    if tool == 1:
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] Calculator selected\n")
        sys_log.close()
        print()
        print('Entering in Calculator...')
        sleep(3)
        print()
        print('Select the calculator type:'
              '\n[1] - Normal calculator;'
              '\n[2] - Binary/Hexadecimal/Octal Calculator;'
              '\n[3] - Exit; ')
        calc_option = int(input('> Option: '))

        if calc_option == 1:
            n1 = float(input('Number 1: '))
            n2 = float(input('Number 2: '))
            print('Operations:'
                  '\n[1] + '
                  '\n[2] - '
                  '\n[3] * '
                  '\n[4] / ')
            operation = int(input('> Operation: '))

            if operation == 1:
                total = n1 + n2
                print(f'Result: {total}.')
            elif operation == 2:
                total = n1 - n2
                print(f'Result: {total}')
            elif operation == 3:
                total = n1 * n2
                print(f'Result: {total}')
            elif operation == 4:
                total = n1 / n2
                print(f'Result: {total}')
        elif calc_option == 2:
            print('[1] - Binary/Hexadecimal/Octal Converter;'
                  '\n[2] - Binary/Hexadecimal/Octal Deconverter;')
            bho_option = int(input('> Option: '))

            if bho_option == 1:
                print('[1] - Binary Converter;'
                      '\n[2] - Hexadecimal Converter;'
                      '\n[3] - Octal converter;')
                bho_converter_option = int(input('> Option: '))
                if bho_converter_option == 1:
                    number = int(input('Number: '))
                    binary = bin(number)[2:]
                    print(f'Number converted to binary: {binary}')

                elif bho_converter_option == 2:
                    number = int(input('Number: '))
                    hexadecimal = hex(number)[2:]
                    print(f'Number converted to hexadecimal: {hexadecimal}')

                elif bho_converter_option == 3:
                    number = int(input('Number: '))
                    octal = oct(number)[2:]
                    print(f'Number converted to octal: {octal}')

            elif bho_option == 2:
                print('[1] - Binary Deconverter;'
                      '\n[2] - Decimal Deconverter;'
                      '\n[3] - Octal Deconverter;')
                bho_converter_option = int(input('> Option: '))

                if bho_converter_option == 1:
                    number = int(input('Number: '))
                    binary_number_deconverted = number & 2
                    print(f'Binary number deconverted: {binary_number_deconverted}')

                elif bho_converter_option == 2:
                    number = int(input('Number: '))
                    hexadecimal_number_deconverted = number & 10
                    print(f'Hexadecimal number deconverted: {hexadecimal_number_deconverted}')

                elif bho_converter_option == 3:
                    number = int(input('Number: '))
                    octal_number_converted = number & 8
                    print(f'Octal number deconverted: {octal_number_converted}')

        elif calc_option == 3:
            print('Quitting Calculator ...')
            sleep(1)
            print('Calculator Quitted.')
    elif tool == 2:
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] Calculator Quitted.")
        sys_log.close()

    while tool != 2:
        print('[1] - Calculator;'
              '\n[2] - Exit')
        tool = int(input('> Option: '))
        if tool == 1:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Calculator selected\n")
            sys_log.close()
            print()
            print('Entering in Calculator...')
            sleep(3)
            print()
            print('Select the calculator type:'
                  '\n[1] - Normal calculator;'
                  '\n[2] - Binary/Hexadecimal/Octal Calculator;'
                  '\n[3] - Exit; ')
            calc_option = int(input('> Option: '))

            if calc_option == 1:
                n1 = float(input('Number 1: '))
                n2 = float(input('Number 2: '))
                print('Operations:'
                      '\n[1] + ;'
                      '\n[2] - '
                      '\n[3] * '
                      '\n[4] / ')
                operation = int(input('> Operation: '))

                if operation == 1:
                    total = n1 + n2
                    print(f'Result: {total}.')
                elif operation == 2:
                    total = n1 - n2
                    print(f'Result: {total}')
                elif operation == 3:
                    total = n1 * n2
                    print(f'Result: {total}')
                elif operation == 4:
                    total = n1 / n2
                    print(f'Result: {total}')
            elif calc_option == 2:
                print('[1] - Binary/Hexadecimal/Octal Converter;'
                      '\n[2] - Binary/Hexadecimal/Octal Deconverter;')
                bho_option = int(input('> Option: '))

                if bho_option == 1:
                    print('[1] - Binary Converter;'
                          '\n[2] - Hexadecimal Converter;'
                          '\n[3] - Octal converter;')
                    bho_converter_option = int(input('> Option: '))
                    if bho_converter_option == 1:
                        number = int(input('Number: '))
                        binary = bin(number)[2:]
                        print(f'Number converted to binary: {binary}')

                    elif bho_converter_option == 2:
                        number = int(input('Number: '))
                        hexadecimal = hex(number)[2:]
                        print(f'Number converted to hexadecimal: {hexadecimal}')

                    elif bho_converter_option == 3:
                        number = int(input('Number: '))
                        octal = oct(number)[2:]
                        print(f'Number converted to octal: {octal}')

                elif bho_option == 2:
                    print('[1] - Binary Deconverter;'
                          '\n[2] - Decimal Deconverter;'
                          '\n[3] - Octal Deconverter;')
                    bho_converter_option = int(input('> Option: '))

                    if bho_converter_option == 1:
                        number = int(input('Number: '))
                        binary_number_deconverted = number & 2
                        print(f'Binary number deconverted: {binary_number_deconverted}')

                    elif bho_converter_option == 2:
                        number = int(input('Number: '))
                        hexadecimal_number_deconverted = number & 10
                        print(f'Hexadecimal number deconverted: {hexadecimal_number_deconverted}')

                    elif bho_converter_option == 3:
                        number = int(input('Number: '))
                        octal_number_converted = number & 8
                        print(f'Octal number deconverted: {octal_number_converted}')

            elif calc_option == 3:
                print('Quitting Calculator ...')
                sleep(1)
                print('Calculator Quitted.')

        elif tool == 2:
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))

            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] Calculator Quitted.")
            sys_log.close()

