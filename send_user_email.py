import smtplib
from time import sleep
import socket


def send_user_email():
    host = '8.8.8.8'
    port = 53
    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

    except socket.error:
        print('MikkOS cannot establish an internet connection using this device. Please make sure your '
              'device is connected to the internet, and if the error persists please contact the '
              'MikkOS support team.')
    else:
        try:
            print("Email Help Categories:"
                  "\n[1] - MikkOS Tools;"
                  "\n[2] - User Logs;"
                  "\n[3] - Exit")
            option = int(input('> Category: '))
            if option == 1:
                print("Select the tool that you are having problems with: "
                      "\n[1] - Site Tools;"
                      "\n[2] - Calculator;"
                      "\n[3] - IPv4/IPv6 Generator;"
                      "\n[4] - Internet Speed Tester;"
                      "\n[5] - What's My IP; "
                      "\n[6] - Random Password Generator")
                tool = int(input('> Option: '))
                if tool == 1:
                    print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools')
                    print('Tools:'
                          '\n[1] - Site Connectivity Checker;'
                          '\n[2] - Host IP;'
                          '\n[3] - Port Scanner;')
                    tool_option = int(input('> Option: '))

                    if tool_option == 1:
                        print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Site Connectivity Checker')
                        print("[1] - The tool 'Site Connectivity Checker' doesn't work;"
                              "\n[2] - The tool 'Site Connectivity Checker' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print('We will not collect your personal data! Type credentialhelp on email field too see '
                                      'why you need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Site Connectivity Checker' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print('We will not collect your personal data! Type credentialhelp on email field too see '
                                      'why you need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Site Connectivity Checker' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Site Connectivity Checker' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Site Connectivity Checker' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                    if tool_option == 2:
                        print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Host IP')
                        print("[1] - The tool 'Host IP' doesn't work;"
                              "\n[2] - The tool 'Host IP' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Host IP' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Host IP' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Host IP' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Host IP' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                    if tool_option == 3:
                        print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Port Scanner')
                        print("[1] - The tool 'Port Scanner' doesn't work;"
                              "\n[2] - The tool 'Port Scanner' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Port Scanner' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Port Scanner' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Port Scanner' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Port Scanner' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                if tool == 2:
                    print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools')
                    print('Tools:'
                          '\n[1] - Normal Calculator;'
                          '\n[2] - Binary/Hexadecimal/Octal Calculator;'
                          '\n[3] - Port Scanner;')
                    tool_option = int(input('> Option: '))

                    if tool_option == 1:
                        print('Email Help Categories -> MikkOS Tools -> Normal Calculator -> Tools -> Normal Calculator')
                        print("[1] - The tool 'Normal Calculator' doesn't work;"
                              "\n[2] - The tool 'Normal Calculator' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Normal Calculator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Normal Calculator' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Normal Calculator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Normal Calculator' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                    if tool_option == 2:
                        print(
                            'Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Binary/Hexadecimal/Octal Calculator')
                        print('Which of the 3 calculators are you having problems with?'
                              '\n[1] - Binary Calculator;'
                              '\n[2] - Hexadecimal Calculator;'
                              '\n[3] - Octal Calculator;')
                        calculator = int(input('> Option: '))

                        if calculator == 1:
                            print("[1] - The tool 'Binary Calculator' doesn't work;"
                                  "\n[2] - The tool 'Binary Calculator' has got one or more bugs.")
                            tool_option_number = int(input('> Option: '))

                            if tool_option_number == 1:
                                extra_information_option = str(
                                    input('Do you wanna give extra information about your problem? '
                                          '[Y] - Yes / [N] - No: ')).upper()
                                if extra_information_option == 'Y':
                                    extra_information = str(input('Extra information: '))
                                    print('Extra Information Added.')
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Binary Calculator' doesn't work."
                                                        f"\nExtra Information: {extra_information}")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")

                                if extra_information_option == 'N':
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Binary Calculator' doesn't work.")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")
                            if tool_option_number == 2:
                                extra_information_option = str(
                                    input('Do you wanna give extra information about your problem? '
                                          '[Y] - Yes / [N] - No: ')).upper()
                                if extra_information_option == 'Y':
                                    extra_information = str(input('Extra information: '))
                                    print('Extra Information Added.')
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Binary Calculator' doesn't work."
                                                        f"\nExtra Information: {extra_information}")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")
                                if extra_information_option == 'N':
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')
                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Binary Calculator' has got one or more bugs.")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")

                        if calculator == 2:
                            print("[1] - The tool 'Hexadecimal Calculator' doesn't work;"
                                  "\n[2] - The tool 'Hexadecimal Calculator' has got one or more bugs.")
                            tool_option_number = int(input('> Option: '))

                            if tool_option_number == 1:
                                extra_information_option = str(
                                    input('Do you wanna give extra information about your problem? '
                                          '[Y] - Yes / [N] - No: ')).upper()
                                if extra_information_option == 'Y':
                                    extra_information = str(input('Extra information: '))
                                    print('Extra Information Added.')
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Hexadecimal Calculator' doesn't work."
                                                        f"\nExtra Information: {extra_information}")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")

                                if extra_information_option == 'N':
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Hexadecimal Calculator' doesn't work.")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")
                            if tool_option_number == 2:
                                extra_information_option = str(
                                    input('Do you wanna give extra information about your problem? '
                                          '[Y] - Yes / [N] - No: ')).upper()
                                if extra_information_option == 'Y':
                                    extra_information = str(input('Extra information: '))
                                    print('Extra Information Added.')
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Hexadecimal Calculator' doesn't work."
                                                        f"\nExtra Information: {extra_information}")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")
                                if extra_information_option == 'N':
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')
                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Hexadecimal Calculator' has got one or more bugs.")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")

                        if calculator == 3:
                            print("[1] - The tool 'Octal Calculator' doesn't work;"
                                  "\n[2] - The tool 'Octal Calculator' has got one or more bugs.")
                            tool_option_number = int(input('> Option: '))

                            if tool_option_number == 1:
                                extra_information_option = str(input('Do you wanna give extra information about '
                                                                     'your problem? [Y] - Yes / [N] - No: ')).upper()
                                if extra_information_option == 'Y':
                                    extra_information = str(input('Extra information: '))
                                    print('Extra Information Added.')
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Octal Calculator' doesn't work."
                                                        f"\nExtra Information: {extra_information}")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")

                                if extra_information_option == 'N':
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Octal Calculator' doesn't work.")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")
                            if tool_option_number == 2:
                                extra_information_option = str(
                                    input('Do you wanna give extra information about your problem? '
                                          '[Y] - Yes / [N] - No: ')).upper()
                                if extra_information_option == 'Y':
                                    extra_information = str(input('Extra information: '))
                                    print('Extra Information Added.')
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')

                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Octal Calculator' doesn't work."
                                                        f"\nExtra Information: {extra_information}")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")

                                if extra_information_option == 'N':
                                    print(
                                        'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                        'need to put your email and password.')
                                    user_email = str(input('Enter your email: '))

                                    if user_email != 'credentialhelp':
                                        user_password = str(input('Enter your password: '))
                                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        server.login(user_email, user_password)
                                        server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                        "The tool 'Octal Calculator' has got one or more bugs.")
                                        print(f'Email sent! We will reply as soon as possible.')
                                        server.quit()

                                    if user_email == 'credentialhelp':
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")

                if tool == 3:
                    print('Email Help Categories -> MikkOS Tools -> IP Generator -> Tools')
                    print('Tools:'
                          '\n[1] - IPv4 Generator;'
                          '\n[2] - IPv6 Generator;')
                    tool_option = int(input('> Option: '))

                    if tool_option == 1:
                        print('Email Help Categories -> MikkOS Tools -> IP Generator -> Tools -> IPv4 Generator')
                        print("[1] - The tool 'IPv4 Generator' doesn't work;"
                              "\n[2] - The tool 'IPv4 Generator' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv4 Generator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv4 Generator' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv4 Generator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv4 Generator' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                    if tool_option == 2:
                        print('Email Help Categories -> MikkOS Tools -> IP Generator -> Tools -> IPv6 Generator')
                        print("[1] - The tool 'IPv6 Generator' doesn't work;"
                              "\n[2] - The tool 'IPv6 Generator' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv6 Generator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv6 Generator' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv6 Generator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'IPv6 Generator' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                if tool == 4:
                    print('Email Help Categories -> MikkOS Tools -> Internet Speed Tester -> Tools')
                    print('Tools:'
                          '\n[1] - Download Speed Tester;'
                          '\n[2] - Upload Speed Tester;')
                    tool_option = int(input('> Option: '))

                    if tool_option == 1:
                        print('Email Help Categories -> MikkOS Tools -> IP Generator -> Tools -> Download Speed Tester')
                        print("[1] - The tool 'Download Speed Tester' doesn't work;"
                              "\n[2] - The tool 'Download Speed Tester' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Download Speed Tester' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Download Speed Tester' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Download Speed Tester' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Download Speed Tester' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                    if tool_option == 2:
                        print(
                            'Email Help Categories -> MikkOS Tools -> Internet Speed Tester -> Tools -> Upload Speed Tester')
                        print("[1] - The tool 'Upload Speed Tester' doesn't work;"
                              "\n[2] - The tool 'Upload Speed Tester' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Upload Speed Tester' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Upload Speed Tester' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Upload Speed Tester' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Upload Speed Tester' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                if tool == 5:
                    print("Email Help Categories -> MikkOS Tools -> What's My IP -> Tools")
                    print("Tools: "
                          "\n[1] - What's My IP?")

                    tool_option = int(input('> Option: '))

                    if tool_option == 1:
                        print("Email Help Categories -> MikkOS Tools -> What's My IP -> Tools -> What's My IP")
                        print("[1] - The tool 'What's My IP' doesn't work;"
                              "\n[2] - The tool 'What's My IP' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'What's My IP' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'What's My IP' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'What's My IP' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'What's My IP' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                if tool == 6:
                    print("Email Help Categories -> MikkOS Tools -> Random Password Generator -> Tools")
                    print("Tools: "
                          "\n[1] - Random Password Generator;")

                    tool_option = int(input('> Option: '))

                    if tool_option == 1:
                        print("Email Help Categories -> MikkOS Tools -> Random Password Generator -> Tools "
                              "-> Random Password Generator ")
                        print("[1] - The tool 'Random Password Generator' doesn't work;"
                              "\n[2] - The tool 'Random Password Generator' has got one or more bugs.")
                        tool_option_number = int(input('> Option: '))

                        if tool_option_number == 1:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Random Password Generator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')

                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Random Password Generator' doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                        if tool_option_number == 2:
                            extra_information_option = str(input('Do you wanna give extra information about your problem? '
                                                                 '[Y] - Yes / [N] - No: ')).upper()
                            if extra_information_option == 'Y':
                                extra_information = str(input('Extra information: '))
                                print('Extra Information Added.')
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Random Password Generator' doesn't work."
                                                    f"\nExtra Information: {extra_information}")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                            if extra_information_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))

                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The tool 'Random Password Generator' has got one or more bugs.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

            if option == 2:
                print("[1] Log file doesn't work;"
                      "\n[2] - Log file has got one or more bugs.")
                log_option = int(input('> Option: '))

                if log_option == 1:
                    log_reason_option = str(input('Do you wanna give extra information about your problem? '
                                                  '[Y] - Yes / [N] - No: ')).upper()

                    if log_reason_option == 'Y':
                        log_reason = str(input('Extra Information: '))
                        print('We will not collect your personal data! Type credentialhelp on email field too see why you'
                              'need to put your email and password.')
                        user_email = str(input('Enter your email: '))
                        if user_email != 'credentialhelp':
                            user_password = str(input('Enter your password: '))
                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                            server.login(user_email, user_password)
                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                            "The Log File doesn't work.")
                            print(f'Email sent! We will reply as soon as possible.')
                            server.quit()

                        if user_email == 'credentialhelp':
                            print("MikkOS has a function that provides the user with the option of "
                                  "sending an email to MikkOS support, without having to access their "
                                  "online email platform. No user information is collected. The user "
                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                  "that logs in only during the time of sending the email with the "
                                  "user's email account in order to send the email, and after that he "
                                  "logs out to always, until the user decides to send an email to "
                                  "MikkOS support using MikkOS again.")

                    if log_reason_option == 'N':
                        print('We will not collect your personal data! Type credentialhelp on email field too see why you'
                              'need to put your email and password.')
                        user_email = str(input('Enter your email: '))
                        if user_email != 'credentialhelp':
                            user_password = str(input('Enter your password: '))
                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                            server.login(user_email, user_password)
                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                            "The Log File doesn't work.")
                            print(f'Email sent! We will reply as soon as possible.')
                            server.quit()

                        if user_email == 'credentialhelp':
                            print("MikkOS has a function that provides the user with the option of "
                                  "sending an email to MikkOS support, without having to access their "
                                  "online email platform. No user information is collected. The user "
                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                  "that logs in only during the time of sending the email with the "
                                  "user's email account in order to send the email, and after that he "
                                  "logs out to always, until the user decides to send an email to "
                                  "MikkOS support using MikkOS again.")

            if option == 3:
                print('Quitting Help Email...')
                sleep(1)
                print('Help Email Quitted')

            while option != 3:
                def send_user_email():
                    print("Email Help Categories:"
                          "\n[1] - MikkOS Tools;"
                          "\n[2] - User Logs;"
                          "\n[3] - Exit")
                    option = int(input('> Category: '))
                    if option == 1:
                        print("Select the tool that you are having problems with: "
                              "\n[1] - Site Tools;"
                              "\n[2] - Calculator;"
                              "\n[3] - IPv4/IPv6 Generator;"
                              "\n[4] - Internet Speed Tester;"
                              "\n[5] - What's My IP;"
                              "\n[6] - Password Generator;")
                        tool = int(input('> Option: '))
                        if tool == 1:
                            print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools')
                            print('Tools:'
                                  '\n[1] - Site Connectivity Checker;'
                                  '\n[2] - Host IP;'
                                  '\n[3] - Port Scanner;')
                            tool_option = int(input('> Option: '))

                            if tool_option == 1:
                                print(
                                    'Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Site Connectivity Checker')
                                print("[1] - The tool 'Site Connectivity Checker' doesn't work;"
                                      "\n[2] - The tool 'Site Connectivity Checker' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print("MikkOS has a function that provides the user with the option of "
                                              "sending an email to MikkOS support, without having to access their "
                                              "online email platform. No user information is collected. The user "
                                              "has to enter his email and password, as MikkOS uses an algorithm "
                                              "that logs in only during the time of sending the email with the "
                                              "user's email account in order to send the email, and after that he "
                                              "logs out to always, until the user decides to send an email to "
                                              "MikkOS support using MikkOS again.")
                                        user_email = str(input('Enter your email: '))
                                        user_password = str(input('Enter your password: '))

                                        if user_email != 'credentialhelp':
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Site Connectivity Checker' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Site Connectivity Checker' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Site Connectivity Checker' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Site Connectivity Checker' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                            if tool_option == 2:
                                print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Host IP')
                                print("[1] - The tool 'Host IP' doesn't work;"
                                      "\n[2] - The tool 'Host IP' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Host IP' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Host IP' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Host IP' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Host IP' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                            if tool_option == 3:
                                print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Port Scanner')
                                print("[1] - The tool 'Port Scanner' doesn't work;"
                                      "\n[2] - The tool 'Port Scanner' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Port Scanner' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Port Scanner' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Port Scanner' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Port Scanner' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                        if tool == 2:
                            print('Email Help Categories -> MikkOS Tools -> Site Tools -> Tools')
                            print('Tools:'
                                  '\n[1] - Normal Calculator;'
                                  '\n[2] - Binary/Hexadecimal/Octal Calculator;'
                                  '\n[3] - Port Scanner;')
                            tool_option = int(input('> Option: '))

                            if tool_option == 1:
                                print(
                                    'Email Help Categories -> MikkOS Tools -> Normal Calculator -> Tools -> Normal Calculator')
                                print("[1] - The tool 'Normal Calculator' doesn't work;"
                                      "\n[2] - The tool 'Normal Calculator' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Normal Calculator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Normal Calculator' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Normal Calculator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Normal Calculator' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                            if tool_option == 2:
                                print(
                                    'Email Help Categories -> MikkOS Tools -> Site Tools -> Tools -> Binary/Hexadecimal/Octal Calculator')
                                print('Which of the 3 calculators are you having problems with?'
                                      '\n[1] - Binary Calculator;'
                                      '\n[2] - Hexadecimal Calculator;'
                                      '\n[3] - Octal Calculator;')
                                calculator = int(input('> Option: '))
                                if calculator == 1:
                                    print("[1] - The tool 'Binary Calculator' doesn't work;"
                                          "\n[2] - The tool 'Binary Calculator' has got one or more bugs.")
                                    tool_option_number = int(input('> Option: '))

                                    if tool_option_number == 1:
                                        extra_information_option = str(
                                            input('Do you wanna give extra information about your problem? '
                                                  '[Y] - Yes / [N] - No: ')).upper()
                                        if extra_information_option == 'Y':
                                            extra_information = str(input('Extra information: '))
                                            print('Extra Information Added.')
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Binary Calculator' doesn't work."
                                                                f"\nExtra Information: {extra_information}")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                        if extra_information_option == 'N':
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Binary Calculator' doesn't work.")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                    if tool_option_number == 2:
                                        extra_information_option = str(
                                            input('Do you wanna give extra information about your problem? '
                                                  '[Y] - Yes / [N] - No: ')).upper()

                                        if extra_information_option == 'Y':
                                            extra_information = str(input('Extra information: '))
                                            print('Extra Information Added.')
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Binary Calculator' doesn't work."
                                                                f"\nExtra Information: {extra_information}")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")
                                        if extra_information_option == 'N':
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')
                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Binary Calculator' has got one or more bugs.")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                if calculator == 2:
                                    print("[1] - The tool 'Hexadecimal Calculator' doesn't work;"
                                          "\n[2] - The tool 'Hexadecimal Calculator' has got one or more bugs.")
                                    tool_option_number = int(input('> Option: '))

                                    if tool_option_number == 1:
                                        extra_information_option = str(
                                            input('Do you wanna give extra information about your problem? '
                                                  '[Y] - Yes / [N] - No: ')).upper()
                                        if extra_information_option == 'Y':
                                            extra_information = str(input('Extra information: '))
                                            print('Extra Information Added.')
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Hexadecimal Calculator' doesn't work."
                                                                f"\nExtra Information: {extra_information}")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                        if extra_information_option == 'N':
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Hexadecimal Calculator' doesn't work.")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                    if tool_option_number == 2:
                                        extra_information_option = str(
                                            input('Do you wanna give extra information about your problem? '
                                                  '[Y] - Yes / [N] - No: ')).upper()
                                        if extra_information_option == 'Y':
                                            extra_information = str(input('Extra information: '))
                                            print('Extra Information Added.')
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Hexadecimal Calculator' doesn't work."
                                                                f"\nExtra Information: {extra_information}")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")
                                        if extra_information_option == 'N':
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')
                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Hexadecimal Calculator' has got one or more bugs.")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                if calculator == 3:
                                    print("[1] - The tool 'Octal Calculator' doesn't work;"
                                          "\n[2] - The tool 'Octal Calculator' has got one or more bugs.")
                                    tool_option_number = int(input('> Option: '))

                                    if tool_option_number == 1:
                                        extra_information_option = str(
                                            input('Do you wanna give extra information about your problem? '
                                                  '[Y] - Yes / [N] - No: ')).upper()
                                        if extra_information_option == 'Y':
                                            extra_information = str(input('Extra information: '))
                                            print('Extra Information Added.')
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Octal Calculator' doesn't work."
                                                                f"\nExtra Information: {extra_information}")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                        if extra_information_option == 'N':
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Octal Calculator' doesn't work.")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                    if tool_option_number == 2:
                                        extra_information_option = str(
                                            input('Do you wanna give extra information about your problem? '
                                                  '[Y] - Yes / [N] - No: ')).upper()
                                        if extra_information_option == 'Y':
                                            extra_information = str(input('Extra information: '))
                                            print('Extra Information Added.')
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')

                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Octal Calculator' doesn't work."
                                                                f"\nExtra Information: {extra_information}")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                                        if extra_information_option == 'N':
                                            print(
                                                'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                                'need to put your email and password.')
                                            user_email = str(input('Enter your email: '))

                                            if user_email != 'credentialhelp':
                                                user_password = str(input('Enter your password: '))
                                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                                server.login(user_email, user_password)
                                                server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                                "The tool 'Octal Calculator' has got one or more bugs.")
                                                print(f'Email sent! We will reply as soon as possible.')
                                                server.quit()

                                            if user_email == 'credentialhelp':
                                                print("MikkOS has a function that provides the user with the option of "
                                                      "sending an email to MikkOS support, without having to access their "
                                                      "online email platform. No user information is collected. The user "
                                                      "has to enter his email and password, as MikkOS uses an algorithm "
                                                      "that logs in only during the time of sending the email with the "
                                                      "user's email account in order to send the email, and after that he "
                                                      "logs out to always, until the user decides to send an email to "
                                                      "MikkOS support using MikkOS again.")

                        if tool == 3:
                            print('Email Help Categories -> MikkOS Tools -> IP Generator -> Tools')
                            print('Tools:'
                                  '\n[1] - IPv4 Generator;'
                                  '\n[2] - IPv6 Generator;')
                            tool_option = int(input('> Option: '))

                            if tool_option == 1:
                                print('Email Help Categories -> MikkOS Tools -> IP Generator -> Tools -> IPv4 Generator')
                                print("[1] - The tool 'IPv4 Generator' doesn't work;"
                                      "\n[2] - The tool 'IPv4 Generator' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))
                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv4 Generator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv4 Generator' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv4 Generator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too'
                                            ' see why you need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv4 Generator' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                            if tool_option == 2:
                                print('Email Help Categories -> MikkOS Tools -> IP Generator -> Tools -> IPv6 Generator')
                                print("[1] - The tool 'IPv6 Generator' doesn't work;"
                                      "\n[2] - The tool 'IPv6 Generator' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()

                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print('We will not collect your personal data! Type credentialhelp on email field '
                                              'too see why you need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv6 Generator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                                    if extra_information_option == 'N':
                                        print('We will not collect your personal data! Type credentialhelp on email field '
                                              'too see why you need to put your email and password.')

                                        user_email = str(input('Enter your email: '))
                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv6 Generator' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                                if tool_option_number == 2:
                                    extra_information_option = str(input('Do you wanna give extra information about your '
                                                                         'problem? [Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print('We will not collect your personal data! Type credentialhelp on email field '
                                              'too see why you need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv6 Generator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))
                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'IPv6 Generator' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                        if tool == 4:
                            print('Email Help Categories -> MikkOS Tools -> Internet Speed Tester -> Tools')
                            print('Tools:'
                                  '\n[1] - Download Speed Tester;'
                                  '\n[2] - Upload Speed Tester;')
                            tool_option = int(input('> Option: '))

                            if tool_option == 1:
                                print(
                                    'Email Help Categories -> MikkOS Tools -> IP Generator -> Tools -> Download Speed Tester')
                                print("[1] - The tool 'Download Speed Tester' doesn't work;"
                                      "\n[2] - The tool 'Download Speed Tester' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))
                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Download Speed Tester' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))
                                        user_password = str(input('Enter your password: '))

                                        if user_email != 'credentialhelp':
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Download Speed Tester' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))
                                        user_password = str(input('Enter your password: '))

                                        if user_email != 'credentialhelp':
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Download Speed Tester' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))
                                        user_password = str(input('Enter your password: '))

                                        if user_email != 'credentialhelp':
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Download Speed Tester' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                            if tool_option == 2:
                                print(
                                    'Email Help Categories -> MikkOS Tools -> Internet Speed Tester -> Tools -> Upload '
                                    'Speed Tester')
                                print("[1] - The tool 'Upload Speed Tester' doesn't work;"
                                      "\n[2] - The tool 'Upload Speed Tester' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Upload Speed Tester' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Upload Speed Tester' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))
                                        user_password = str(input('Enter your password: '))

                                        if user_email != 'credentialhelp':
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Upload Speed Tester' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))
                                        user_password = str(input('Enter your password: '))

                                        if user_email != 'credentialhelp':
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Upload Speed Tester' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of sending"
                                                  " an email to MikkOS support, without having to access their online email"
                                                  " platform. No user information is collected. The user has to enter his"
                                                  " email and password, as MikkOS uses an algorithm that logs in only"
                                                  "during the time of sending the email with the user's email account in"
                                                  "order to send the email, and after that he logs out to always, until the"
                                                  "user decides to send an email to MikkOS support using MikkOS again.")

                        if tool == 5:
                            print("Email Help Categories -> MikkOS Tools -> What's My IP -> Tools")
                            print("Tools: "
                                  "\n[1] - What's My IP?")

                            tool_option = int(input('> Option: '))

                            if tool_option == 1:
                                print("Email Help Categories -> MikkOS Tools -> IP Generator -> Tools -> What's My IP")
                                print("[1] - The tool 'What's My IP' doesn't work;"
                                      "\n[2] - The tool 'What's My IP' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'What's My IP' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'What's My IP' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'What's My IP' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'What's My IP' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                        if tool == 6:
                            print("Email Help Categories -> MikkOS Tools -> Random Password Generator -> Tools")
                            print("Tools: "
                                  "\n[1] - Random Password Generator")

                            tool_option = int(input('> Option: '))

                            if tool_option == 1:
                                print("Email Help Categories -> MikkOS Tools -> Random Password Generator -> Tools "
                                      "-> Random Password Generator ")
                                print("[1] - The tool 'Random Password Generator' doesn't work;"
                                      "\n[2] - The tool 'Random Password Generator' has got one or more bugs.")
                                tool_option_number = int(input('> Option: '))

                                if tool_option_number == 1:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Random Password Generator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")
                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')

                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Random Password Generator' doesn't work.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                                if tool_option_number == 2:
                                    extra_information_option = str(
                                        input('Do you wanna give extra information about your problem? '
                                              '[Y] - Yes / [N] - No: ')).upper()
                                    if extra_information_option == 'Y':
                                        extra_information = str(input('Extra information: '))
                                        print('Extra Information Added.')
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Random Password Generator' doesn't work."
                                                            f"\nExtra Information: {extra_information}")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                                    if extra_information_option == 'N':
                                        print(
                                            'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                            'need to put your email and password.')
                                        user_email = str(input('Enter your email: '))

                                        if user_email != 'credentialhelp':
                                            user_password = str(input('Enter your password: '))
                                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                            server.login(user_email, user_password)
                                            server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                            "The tool 'Random Password Generator' has got one or more bugs.")
                                            print(f'Email sent! We will reply as soon as possible.')
                                            server.quit()

                                        if user_email == 'credentialhelp':
                                            print("MikkOS has a function that provides the user with the option of "
                                                  "sending an email to MikkOS support, without having to access their "
                                                  "online email platform. No user information is collected. The user "
                                                  "has to enter his email and password, as MikkOS uses an algorithm "
                                                  "that logs in only during the time of sending the email with the "
                                                  "user's email account in order to send the email, and after that he "
                                                  "logs out to always, until the user decides to send an email to "
                                                  "MikkOS support using MikkOS again.")

                    if option == 2:
                        print("[1] Log file doesn't work;"
                              "\n[2] - Log file has got one or more bugs.")
                        log_option = int(input('> Option: '))

                        if log_option == 1:
                            log_reason_option = str(input('Do you wanna give extra information about your problem? '
                                                          '[Y] - Yes / [N] - No: ')).upper()

                            if log_reason_option == 'Y':
                                log_reason = str(input('Extra Information: '))
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))
                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The Log File doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")

                            if log_reason_option == 'N':
                                print(
                                    'We will not collect your personal data! Type credentialhelp on email field too see why you'
                                    'need to put your email and password.')
                                user_email = str(input('Enter your email: '))
                                if user_email != 'credentialhelp':
                                    user_password = str(input('Enter your password: '))
                                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                    server.login(user_email, user_password)
                                    server.sendmail(user_email, 'mikkosofficial@gmail.com',
                                                    "The Log File doesn't work.")
                                    print(f'Email sent! We will reply as soon as possible.')
                                    server.quit()

                                if user_email == 'credentialhelp':
                                    print("MikkOS has a function that provides the user with the option of "
                                          "sending an email to MikkOS support, without having to access their "
                                          "online email platform. No user information is collected. The user "
                                          "has to enter his email and password, as MikkOS uses an algorithm "
                                          "that logs in only during the time of sending the email with the "
                                          "user's email account in order to send the email, and after that he "
                                          "logs out to always, until the user decides to send an email to "
                                          "MikkOS support using MikkOS again.")
                    if option == 3:
                        print('Quitting Help Email...')
                        sleep(1)
                        print('Help Email Quitted')

        except smtplib.SMTPAuthenticationError:
            print("Error! MikkOS was unable to log into your account. Disable the 'Less secure apps' option in your "
                  "account. You can allow this option by entering this link: https://myaccount.google.com/lesssecureapps "
                  "Please try again.")
