import socket

while True:

    print('Connecting')


    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("localhost", 3333))
        except ConnectionRefusedError:
            continue
        else:
            print('Connected')
            break


    x = input('Send Message: ')





    str_recv = s.recv(1024)

    print(str(str_recv))

    str_send = "Hello, the world!"

    s.send(bytes(x, 'utf-8'))

    str_recv = s.recv(1024)

    # print(str(str_recv, 'utf-8'))
    print(str(str_recv, 'utf-8'))
    s.close()
