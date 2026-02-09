def main():
    # import sys
    #             sys.argv[1]
    nomefile = "logfile.txt"
    try:
        f=open(nomefile, "r", encoding='utf-8')
        righe=f.readlines()
        for riga in righe:
            print(riga, end='')
    except FileNotFoundError as e:
        print(f"[-] errore bloccante: {str(e)}")
        
if __name__ == "__main__":
    main()