import socket
import datetime
import time

t = 0

while True:
    print('Connecting')
    try:
        print('Connecting')
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(('localhost', 3333))
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except socket.error:
                print('socket.error, Retrying', t)
                time.sleep(0.1)
                t += 1
                continue
            else:
                print('Succsess', datetime.datetime.time(datetime.datetime.now()))
                break

            print('# DEBUG: 1')
            print(datetime.datetime.time(datetime.datetime.now()))
            s.listen(5)
            print('# DEBUG: 2')
            print(datetime.datetime.time(datetime.datetime.now()))

            flag = 0
            while True:
                connect, addr = s.accept()
                print("Connection Address:" + str(addr))
                print(datetime.datetime.time(datetime.datetime.now()))

                str_return = "Welcome to visit my test socket server. Waiting for command."
                connect.sendto(bytes(str_return, 'utf-8'), addr)

                str_recv, temp = connect.recvfrom(1024)
                print(str(str_recv, 'utf-8'))

                str_return = "I got your command, it is " + str(str_recv, 'utf-8')
                connect.sendto(bytes(str_return, 'utf-8'), addr)
                # str_return = "Received at " + datetime.datetime.time(datetime.datetime.now())
                # connect.sendto(bytes(str_return, 'utf-8'), addr)

                connect.close()
    except ConnectionResetError:
        print('Connection Reset. Retrying')
        continue
