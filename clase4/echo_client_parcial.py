import socket

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5500)

    print(f"[*] Conectando a servidor en {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "hola mundo!"
    msg_bytes = msg.encode("utf-8")
    cantidad_esperada = len(msg_bytes)
    cantidad_recibida = 0
    msg_recibido_bytes = 'b'

    print(f"[*] Preparándome para enviar {msg}")
    sock.sendall("utf-8")

    while cantidad_recibida < cantidad_esperada:
        data = sock.recv(SOCK_BUFFER)
        print(f"[!] Recibi: {data}")
        msg_recibido_bytes += data
        cantidad_recibida += len(data)

    print(f"[*] Terminando operacion, cerrando el socket")
    sock.close()

    print(f"[*] Mensaje total recibido: {msg_recibido_bytes.decode('utf-8')}")



    # Para laboratorio: 
    # socket server del archivo de notas (notas arqui.csv) hacer dos versiones del servidor 1 retornar todas las notas para q el cliente pueda calcular la nota final
    # 2 programas de servidor, calcular tiempos de ejecucion para el cliente en varios escenarios 


    ## servidor = recibe codigo pucp, el primer programa buscara las notas en el archivo, con el codigo y devolvera todas las notas. El cliente usara esto para calcular ...

    # evaluar tiempos de ejecucion 
