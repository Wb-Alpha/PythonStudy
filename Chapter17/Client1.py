import socket
s = socket.socket()             #创建TCP/IP套接字
host = socket.gethostname()     #获取主机地址
port = 12345                    #设置端口号
s.connet((host, port))          #主动初始化TCP服务器连接
