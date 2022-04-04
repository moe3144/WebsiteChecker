#!/usr/bin/python3

from server import Server

print("*** Simple Website Status Checker ***")
print("Checks if website is up and running. \n")

if __name__ == "__main__":
    exit = False
    while (exit == False):
        try:
            host = str(input("Enter Website name: ")).strip()
        except ValueError:
            print("Please Enter String Value.")
            continue
        
        try:
            port = int(input("Enter Port Number: "))
        except ValueError:
            print("Please Enter Integer Value.")
            continue
        
     
        else:
            client = Server(host, port)
            if client.is_running():
                client.status = "Reachable"
            else:
                client.status = "Unreachable"
            print(client)

        if input("Would like to try another Website (Y/N): ") in {'n', 'N'}:
            exit = True
    
