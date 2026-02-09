def main():
    import socket
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 7654
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, addr_p = server_socket.accept()
    print(f"Connected by {addr_p}\n") #tupla, non modficabile
    # conn.sendall('Indicami il tuo username'.encode()). si può usare anche così, ma è più semplice usare i byte (b) direttamente
    conn.sendall(b'Indicami il tuo username: ')
    username = conn.recv(1024).decode()
    print(f"Username ricevuto: {username}\n")
    conn.sendall(b'Indicami la tua password: ')
    password = conn.recv(1024).decode()
    print(f"Password ricevuta: {password}\n")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()