import socket
while True:

    x = input('Send Message: ')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("localhost", 3333))

    str_recv = s.recv(1024)

    print(str(str_recv))

    str_send = "Hello, the world!"

    # s.send(bytes(str_send, 'utf-8'))
    s.send(bytes(x, 'utf-8'))

    str_recv = s.recv(1024)

    print(str(str_recv, 'utf-8'))
    s.close()
