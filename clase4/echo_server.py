import socket

SOCKET_BUFFER = 1024

# trabajare con AF_INET para este caso, solo usamos ipv4

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #este es el objeto
    #server data, lo que se hace es atar el puerto al socket
    server_adress = ('0.0.0.0', 5500)
    print(f"[*] Levantando servidor en direccion {server_adress[0]}:{server_adress[1]}")

    sock.bind(server_adress)
# servidor como tal es un programa, el socket no te define un servidor. 
# bind se designa el socket como tal para poder escuchar de este
# en el servidor se usa bind, bind = atar

    sock.listen(5)
        #backlog: ^clientes en espera
         
# todo lo que recibo lo retorno 
    while True: 
        print("[*] Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexion establecida con {client_address[0]}:{client_address[1]}")

        try:
            while True:
                dato = conn.recv(SOCKET_BUFFER)

                if dato: 
                    print(f"[+] Recibi: {dato}")
                    conn.sendall(dato)
                else:
                    print("No hay mas datos de parte del cliente")
                    break
        except ConnectionResetError:
            print("[!] Cliente cerro la conexion abruptamente")
        finally: 
            print("[*] Cerrando la conexion.")
            sock.close()
