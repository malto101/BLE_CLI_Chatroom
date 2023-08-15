import socket

server = socket.socket(socket.AF_BLUETOOTH,
                       socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("E0:D4:E8:39:2A:41", 4))
server.listen(1)

client, address = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message:{data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
except OSError:
    pass

client.close()
server.close()
