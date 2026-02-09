import socket

def main():
    s=socket.socket()
    indirizzo = "127.0.0.1"
    porta = 7654
    s.connect((indirizzo, porta))
    prompt = s.recv(1024)
    username = input(prompt.decode())
    s.sendall(username.encode())
    prompt = s.recv(1024)
    password = input(prompt.decode())
    s.sendall(password.encode())
    s.close()

if __name__ == "__main__":
    main()    