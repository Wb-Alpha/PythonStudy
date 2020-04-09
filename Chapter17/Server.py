import socket                       #导入socket模块
host = '127.0.0.1'                  #主机IP
port = 8849                         #端口号
web = socket.socket()               #创建socket连接
web.bind((host, port))              #绑定端口
web.listen(5)                       #设置最多连接数
print("服务器等待客户端连接")
#开启死循环
while True:
    conn.addr = web.accept()        #建立客户端连接
    data = conn.recv(1024)          #获取客户端请求数据
    print(data)                     #打印收到的数据
    conn.sendadd(b'HTTP/1.1 200 OK\r\n\r\nClientTrackback')
    conn.close()