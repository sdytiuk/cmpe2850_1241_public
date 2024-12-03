import socket
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Turn off the Nagle algorithm, SEND when I say SEND damn it !
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
    # By default the timeout for calls like connect, send, recv are in seconds.
    # By setting the timeout to None, it turns these calls into Blocking calls, which is fine for our purposes.
    s.settimeout(None)
    s.connect(('localhost', 5000))
    while True:
        time.sleep(10)
        s.sendall("Merry Christmas!".encode('utf-8'))
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
except socket.gaierror:
    print("Invalid address or hostname")
except socket.timeout:
    print("Connection timed out")
except ConnectionRefusedError:
    print("Connection refused by the server")
except Exception as e: # something unexpected
    print("An error occurred:", e)
else:
    print("Connection successful!")
    s.shutdown(socket.SHUT_RDWR) # Disable and shutdown both Rec/Send sides of the socket, close() does do it, but it isn't guaranteed to occur now
    s.close()
