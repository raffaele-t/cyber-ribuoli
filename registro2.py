def main():
    import socket
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 7654
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    # apertura file in scrittura per registrare username e password
    f = open('registro.txt', 'w')
    f.write(f"Server di registrazione in ascolto su {host}:{port}\n")
    f.write("=" * 50 + "\n")
    
    try:
        for i in range(100):  # Allow up to 100 connections
            conn, addr = server_socket.accept()
            f.write(f"\nNuova connessione da {addr}\n")
            
            try:
                # Invia prompt per username senza aspettare
                prompt_username = "Indicami il tuo username: "
                conn.sendall(prompt_username.encode())
                
                # Ricevi username
                username_data = conn.recv(1024)
                if not username_data:
                    break
                username = username_data.decode().strip()
                f.write(f"Username ricevuto: {username}\n")
                
                # Invia prompt per password
                prompt_password = "Scegli una password: "
                conn.sendall(prompt_password.encode())
                
                # Ricevi password
                password_data = conn.recv(1024)
                if not password_data:
                    break
                password = password_data.decode().strip()
                f.write(f"Password ricevuta: {password}\n")
                
                # Conferma registrazione
                risposta = "Registrazione completata con successo!\n"
                conn.sendall(risposta.encode())
                f.write("Registrazione completata\n")
                
            finally:
                conn.close()
    
    finally:
        f.close()
        server_socket.close()

if __name__ == "__main__":
    main()