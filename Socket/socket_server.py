
import socket

import threading
# 类型与类型所用的协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定
server.bind(('0.0.0.0', 8000))
# 监听
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        if data.decode("utf8") == "exit":
            break
        re_data = input()
        sock.send(re_data.encode("utf8"))
    sock.close()


while True:
    sock, addr = server.accept()
    # 用线程处理请求
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()




# # 获取客户端发送的数据 一次获取1k数据
# data = sock.recv(1024)
# # 发送与接收的数据是 byte 型的
# print(data.decode('utf8'))
# # 在接收到数据之后向客户端再发送一个数据
# sock.send("hello,{}".format(data.decode("utf8")).encode("utf8"))
# server.close()
# sock.close()

