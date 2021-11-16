import socket

s=socket.socket()
s.bind(("localhost",8000))
s.listen(5)

while(True):
    conexion,addr=s.accept()
    print("Nueva conexion establecida!")
    print(addr)

    peticion=conexion.recv(1024)
    print(peticion)

    conexion.send(bytes("Hola, te saludo desde el servidor","utf-8"))
    conexion.close()