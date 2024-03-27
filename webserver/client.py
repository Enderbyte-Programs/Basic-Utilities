import socket

s = socket.socket()
s.connect(("216.232.200.238",10223))
s.sendall(b"&&BU$2.31.0$Raspbian Linux 8.3")
s.close()
