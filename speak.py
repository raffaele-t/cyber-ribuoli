import socket
import sys

def main():
    messaggio = sys.argv[1]
    s=socket.socket()
    s.settimeout(2)
    indirizzo = "127.0.0.1"
    porta = 6364
    s.connect((indirizzo, porta))
    s.sendall (messaggio.encode())
    risposta=s.recv(1024)
    print(risposta.decode())
    s.close()

if __name__ == "__main__":
    main()    