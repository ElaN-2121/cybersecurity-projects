import socket
import sys

host = sys.argv[1] if len(sys.argv) >1 else "127.0.0.1"
port=int(sys.argv[2]) if len(sys.argv)>2 else 22

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#AF_INET = IPV4
#SOCK_STREAM = TCP
s.settimeout(1.0) #to stop soon
try:
    s.connect((host, port)) #attempt tcp connect
    print(f"{host}:{port} is OPEN")
except (socket.timeout, ConnectionRefusedError):
    print(f"{host}:{port} is CLOSED or FILTERED")
except Exception as e:
    print("Error:", e)
finally:
    s.close()