import socket


# domain:5000

#AF_INET - IPv4, SOCK_STREAM - TCP
#Если прервать работу скрипта, то порт может быть занят в течение некоторого времени, чтобы данные долшли до адресата
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Чтобы повотрно использовать номер порта
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#К какому домену и порту привязать
server_socket.bind(('localhost', 5000))

#Прослушивание входящего буфера на предмет подключений
server_socket.listen()

#Неизвестно время взаимодействия клиента и сервера
while True:
    #Возвращает клиентский сокет и адрес
    print('Before .accept()')
    #Принимаем входящее подключение
    client_socket, addr = server_socket.accept()
    print('Connectino from', addr)

    while True:
        # print('Before .recv()')
        #Принимаем сообщение от пользователя
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            #Перенос в bites
            response = 'Hello!\n'.encode()
            client_socket.send(response)
        
        print('Outside inner while loop')
        client_socket.close()

'''
Асинхронный код можно писать с помощью:
1) Коллбеков
2) Генераторов и корутин
3) async/await
'''