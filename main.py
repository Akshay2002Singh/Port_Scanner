import socket 
from IPy import IP
import fontstyle

def check_and_convert(ip_add):
    try:
        IP(ip_add)
        return (ip_add)
    except ValueError:
        return socket.gethostbyname(ip_add)

def check_port(t_ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.9)
        sock.connect((t_ip,port))
        print(f"\t[+] Port {port} is open")
    except:
        print(f"\t[+] Port {port} is closed")
        # pass

def scan(temp_ip):
    real_ip = check_and_convert(temp_ip)
    print(f"\n[-] Scanning Target {temp_ip}")
    for port in range(1,65536):
        check_port(real_ip,port)

if __name__=="__main__":
    head = fontstyle.apply("\nELITE PORT SCANNER","bold/Italic/CYAN")
    print(head)
    targets = input('\n[+] Enter Target/s To Scan (split multiple targets with ,) : ')
    if ',' in targets:
        for ip in targets.split(','):
            scan(ip.strip(' '))
    else:
        scan(targets)

