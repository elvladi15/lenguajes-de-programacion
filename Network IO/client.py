import socket

s=socket.socket()
s.connect(("localhost",8000))

s.send(bytes("Hola desde el cliente!","utf-8"))
respuesta=s.recv(1024)

print(respuesta)
s.close()