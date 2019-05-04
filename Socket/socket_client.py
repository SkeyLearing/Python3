import socket

# 类型与类型所用的协议
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接 明确指明IP地址 端口
client.connect(('127.0.0.1', 8000))
while True:
    re_data = input()
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))












# # 发送的时候需要先将数据解码
# client.send("bobby".encode("utf8"))
# data = client.recv(1024)
# print(data.decode("utf8"))
# client.close()