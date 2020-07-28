import socket
m=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
m.connect(('data.pr4e.org', 80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
m.send(cmd)
while True:
    d=m.recv(512)
    if len(d)<1:
        break
    else:
        print(d.decode())
m.close()