import socket
#getting input from user
print("""
██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ ███╗   ██╗
██║ ██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║
█████╔╝ ██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║     ███████║██╔██╗ ██║
██╔═██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██╗██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")

print(" 1.SCAN THE ALL PORT \n 2.SCAN PARTICULAR PORT PRESS \n 3.EXIT")

n=int(input(">"))
#port selection
if(n==2):
    target=input("ENTER THE IP ADDRESS:>")

    start=int(input("ENTER THE PORT FROM:>"))
    stop=int(input("ENTER THE PORT TO:>"))
    print(f"Scanning {target} from port {start} to {stop}...\n")
    for port in range(start,stop+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)
        result = sock.connect_ex((target, port))

        if result==1:
            print(f"[+] Port {port} is OPEN")
if(n==1):
    target=input("ENTER THE IP ADDRESS:>")


    print(f"Scanning {target} from port 1 to 10000...\n")
    for port in range(1,10001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target, port))
        if result==1:
            print(f"[+] Port {port} is OPEN")

if(n==3):
     print("THANK YOU")
else:
    print("INVALID OPTION")



