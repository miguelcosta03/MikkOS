import socket
import smtplib
from datetime import datetime


def user_email_sender():
    date = datetime.now()
    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
    sys_log = open("logs.txt", "a")
    sys_log.write(f"[{sys_date}] - Checked internet connection to use User Email Sender.\n")
    sys_log.close()
    host = '8.8.8.8'
    port = 53

    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

    except socket.error:
        print('MikkOS cannot establish an internet connection using this device. Please make sure your '
              'device is connected to the internet, and if the error persists please contact the '
              'MikkOS support team.')
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Internet Connection Error. No internet connection could be established.")
        sys_log.close()

    else:
        date = datetime.now()
        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
        sys_log = open("logs.txt", "a")
        sys_log.write(f"[{sys_date}] - Sucessfuly internet connection established.\n")
        sys_log.close()

        print('[1] - Send a email;'
              '\n[2] - Exit')
        tool = int(input('> Option: '))
        if tool == 1:
            try:
                sender_email = str(input("Enter the sender's email: "))
                sender_password = str(input("Enter the sender's email password: "))
                receiver_email = str(input("Enter the receiver's email: "))
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(sender_email, sender_password)

            except smtplib.SMTPAuthenticationError:
                print("Sender's email or password incorrect. Please try again.")
                print("If you inserted the right credentials please verify that you have the option 'Less Secure"
                      "Apps' disable in your account.")
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Inserted wrong credentials or user senders account has got Less Secure "
                              f"Apps Allowed")
                sys_log.close()

            else:
                message = str(input('Type your email message here: '))
                server.sendmail(sender_email, receiver_email,
                                message)
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Email sent to {receiver_email}\n")
                sys_log.close()

                print(f'Email sent to {receiver_email}!')
                print('[1] - Send another email;'
                      '\n[2] - Log out and Exit;')
                option = int(input('> Option: '))
                if option == 1:
                    print(f'[1] - Send another email to {receiver_email};'
                          f'\n[2] - Change receiver email;'
                          f'\n[3] - Exit;')
                    tool_option = int(input('> Option: '))
                    while tool != 3:
                        if tool_option == 1:
                            email_sender_password = str(input(f'Enter the {sender_email} password: '))
                            try:
                                email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                email_server.login(sender_email, email_sender_password)

                            except smtplib.SMTPAuthenticationError:
                                print("Sender's email or password incorrect. Please try again.")
                                print("If you inserted the right credentials please verify that you have the option "
                                      "'Less Secure Apps' disable in your account.")
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] - Inserted wrong credentials or user senders "
                                              f"account has got Less Secure Apps Allowed\n")
                                sys_log.close()

                            else:
                                email_message = str(input('Type your email message here: '))
                                email_server.sendmail(sender_email, email_sender_password,
                                                      email_message)
                                print(f'Email sent to {receiver_email}!')
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] - Email sent to {receiver_email}\n")
                                sys_log.close()

                                print('Logging out your account...')
                                print('Sucessful log out your account!')
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] - Logged out account. Account:{sender_email}\n")
                                sys_log.close()

                        if tool_option == 2:
                            email_sender_password = str(input(f'Enter the {sender_email} password: '))
                            receiver_email_account = str(input("Enter the receiver's email: "))
                            try:
                                send_email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                send_email_server.login(sender_email, email_sender_password)

                            except smtplib.SMTPAuthenticationError:
                                print("Sender's email or password incorrect. Please try again.")
                                print("If you inserted the right credentials please verify that you have the option "
                                      "'Less Secure Apps' disable in your account.")
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] - Inserted wrong credentials or user senders "
                                              f"account has got Less Secure Apps Allowed\n")
                                sys_log.close()
                            else:
                                send_email_message = str(input('Type your email message here: '))
                                send_email_server.sendmail(sender_email, receiver_email_account,
                                                           send_email_message)
                                print(f'Email sent to {receiver_email_account}')
                                date = datetime.now()
                                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                sys_log = open("logs.txt", "a")
                                sys_log.write(f"[{sys_date}] - Email sent to {receiver_email}\n")
                                sys_log.close()
                        if tool == 3:
                            print(f'Logging out {sender_email}...')
                            print(f'Succesfully logged out {sender_email}!')
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] - Logged out account. Account:{sender_email}\n")
                            sys_log.close()

                elif option == 2:
                    print('Logging out your account...')
                    print('Sucessful log out your account!')
                    server.quit()
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - Logged out account. Account:{sender_email}\n")
                    sys_log.close()
        if tool == 2:
            print('Quitting User Email Sender Tool...')
            print('User Email Sender Tool Quitted.')
            date = datetime.now()
            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
            sys_log = open("logs.txt", "a")
            sys_log.write(f"[{sys_date}] - User Email Sender Tool Quitted\n")
            sys_log.close()

        while tool != 2:
            host = '8.8.8.8'
            port = 53
            try:
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

            except socket.error:
                print('MikkOS cannot establish an internet connection using this device. Please make sure your '
                      'device is connected to the internet, and if the error persists please contact the '
                      'MikkOS support team.')
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Internet Connection Error. No internet connection could be "
                              f"established.\n")
                sys_log.close()

            else:
                date = datetime.now()
                sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                sys_log = open("logs.txt", "a")
                sys_log.write(f"[{sys_date}] - Sucessfuly internet connection established.\n")
                sys_log.close()

                print('[1] - Send a email;'
                      '\n[2] - Exit')
                tool = int(input('> Option: '))
                if tool == 1:
                    try:
                        sender_email = str(input("Enter the sender's email: "))
                        sender_password = str(input("Enter the sender's email password: "))
                        receiver_email = str(input("Enter the receiver's email: "))
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login(sender_email, sender_password)

                    except smtplib.SMTPAuthenticationError:
                        print("Sender's email or password incorrect. Please try again.")
                        sys_log.write(f"[{sys_date}] - Inserted wrong credentials or user senders "
                                      f"account has got Less Secure Apps Allowed")
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] - Inserted wrong credentials or user senders account has "
                                      f"got Less Secure Apps Allowed\n")
                        sys_log.close()

                    else:
                        message = str(input('Type your email message here: '))
                        server.sendmail(sender_email, receiver_email,
                                        message)
                        print(f'Email sent to {receiver_email}!')
                        date = datetime.now()
                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                        sys_log = open("logs.txt", "a")
                        sys_log.write(f"[{sys_date}] - Email sent to {receiver_email}\n")
                        sys_log.close()

                        print('[1] - Send another email;'
                              '\n[2] - Log out and Exit;')
                        option = int(input('> Option: '))

                        if option == 1:
                            print(f'[1] - Send another email to {receiver_email};'
                                  f'\n[2] - Change receiver email;'
                                  f'\n[3] - Exit;')
                            tool_option = int(input('> Option: '))

                            while tool != 3:
                                if tool_option == 1:
                                    email_sender_password = str(input(f'Enter the {sender_email} password: '))
                                    try:
                                        email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        email_server.login(sender_email, email_sender_password)

                                    except smtplib.SMTPAuthenticationError:
                                        print("Sender's email or password incorrect. Please try again.")
                                        print("If you inserted the right credentials please verify that you have "
                                              "the option 'Less Secure Apps' disable in your account.")
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] - Inserted wrong credentials or user senders "
                                                      f"account has got Less Secure Apps Allowed\n")
                                        sys_log.close()

                                    else:
                                        email_message = str(input('Type your email message here: '))
                                        email_server.sendmail(sender_email, email_sender_password,
                                                              email_message)
                                        print(f'Email sent to {receiver_email}!')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] - Email sent to {receiver_email}\n")
                                        sys_log.close()

                                        print('Logging out your account...')
                                        print('Sucessful log out your account!')

                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] - Logged out account. Account:{sender_email}\n")
                                        sys_log.close()

                                if tool_option == 2:
                                    email_sender_password = str(input(f'Enter the {sender_email} password: '))
                                    receiver_email_account = str(input("Enter the receiver's email: "))
                                    try:
                                        send_email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                        send_email_server.login(sender_email, email_sender_password)

                                    except smtplib.SMTPAuthenticationError:
                                        print("Sender's email or password incorrect. Please try again.")
                                        print("If you inserted the right credentials please verify that you have "
                                              "the option 'Less Secure Apps' disable in your account.")
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] - Inserted wrong credentials or user senders "
                                                      f"account has got Less Secure Apps Allowed\n")
                                        sys_log.close()
                                    else:
                                        send_email_message = str(input('Type your email message here: '))
                                        send_email_server.sendmail(sender_email, receiver_email_account,
                                                                   send_email_message)
                                        print(f'Email sent to {receiver_email_account}')
                                        date = datetime.now()
                                        sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                        sys_log = open("logs.txt", "a")
                                        sys_log.write(f"[{sys_date}] - Email sent to {receiver_email_account}\n")
                                        sys_log.close()
                                if tool == 3:
                                    print(f'Logging out {sender_email}...')
                                    print(f'Succesfully logged out {sender_email}!')
                                    date = datetime.now()
                                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                                    sys_log = open("logs.txt", "a")
                                    sys_log.write(f"[{sys_date}] - Logged out account. Account:{sender_email}\n")
                                    sys_log.close()

                        elif option == 2:
                            print('Logging out your account...')
                            print('Sucessful log out your account!')
                            server.quit()
                            date = datetime.now()
                            sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                            sys_log = open("logs.txt", "a")
                            sys_log.write(f"[{sys_date}] - Logged out account. Account:{sender_email}\n")
                            sys_log.close()

                if tool == 2:
                    print('Quitting User Email Sender Tool...')
                    print('User Email Sender Tool Quitted.')
                    date = datetime.now()
                    sys_date = str(date.strftime("%d-%m-%Y %H:%M:%S"))
                    sys_log = open("logs.txt", "a")
                    sys_log.write(f"[{sys_date}] - User Email Sender Tool Quitted\n")
                    sys_log.close()
