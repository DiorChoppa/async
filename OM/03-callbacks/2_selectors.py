import socket
import selectors


selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # 1- файловый объект (файл с fileno())
    # 2 - событие, которое нас интересует
    # 3 - любьые связанные данные (сессия, id сессии)
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)

def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        # Перенос в bites
        response = 'Ohayo!\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        # (key - SelectorKey (fileobj, events, data), events - битовая маска событий чтения/записи)
        events = selector.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == '__main__':
    server()
    event_loop()