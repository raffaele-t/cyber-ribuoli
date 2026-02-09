def main(): 
    import socket
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 6364
    server_socket.bind((host, port))
    server_socket.listen(1)
    #apertura file in scrittura
    f=open('logfile.txt', "w")
    f.write(f"Server listening on {host}:{port}\n")
    for i in range(100):  # Allow up to 100 connections
        conn, addr = server_socket.accept()
        f.write(f"Connected by {addr}\n")
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                else:
                    richiesta = data.decode()
                    if richiesta == 'SHUTDOWN':
                        break
                    else:
                        risposta = f"Ho ricevuto il tuo messaggio: {richiesta}\n"
                        #print(risposta)
                        f.write(risposta)
                        conn.sendall(risposta.encode())
        finally:
            #chiudere file
            conn.close()
        if richiesta == 'SHUTDOWN':
            break
    f.close()
    server_socket.close()
if __name__ == "__main__":
    main()