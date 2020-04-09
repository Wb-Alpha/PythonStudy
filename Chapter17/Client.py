import socket                       #导入socket模块
s = socket.socket()                 #创建socket连接
host = '127.0.0.1'                  #主机IP
port = 8849                         #端口号
s.connect((host, port))             #主动初始化TCP服务器连接
send_data = input("请输入要发送地数据：")
s.send(send_data.encode())          #发送TCP数据
#接收对方发送过来的数据，最大接受1024个字节
recvData = s.recv(1024).decode()
print('接收的数据为',recvData)
s.close()