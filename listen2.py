def main():
    import socket
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 7654
    utenti = {'admin':'èsegreta'}
    server_socket.bind((host, port))
    server_socket.listen(1)
    for i in range(5):  # Allow up to n connections
        conn, addr_p = server_socket.accept()
        print(f"Connected by {addr_p}\n") #tupla, non modficabile
        # conn.sendall('Indicami il tuo username'.encode()). si può usare anche così, ma è più semplice usare i byte (b) direttamente
        conn.sendall(b'Indicami il tuo username: ')
        username = conn.recv(1024).decode()
        # print(f"Username ricevuto: {username}\n")
        conn.sendall(b'Indicami la tua password: ')
        password = conn.recv(1024).decode()
        # print(f"Password ricevuta: {password}\n")
        if username == 'admin':
            if utenti[username] == password:
                conn.sendall(str(utenti).encode())
                print(f"Utenti registrati: {utenti}\n")
                print("Accesso consentito\n")
            else:
                conn.sendall(b'Accesso negato\n')
                conn.close()
                continue
        else:
            utenti[username] = password #la chiave è l'username, il valore è la password
        conn.close()
    server_socket.close()
    # print(f"Utenti registrati: {utenti}\n")
    # for u, p in utenti.items():
    #     print(f"Username: {u}, Password: {p}\n")

if __name__ == "__main__":
    main()