from asyncio import events
from re import L
import sys
import socket
import selectors
import types

sel  = selectors.DefaultSelector()

def connect_wrapper(sock):
    conn,addr = sock.accept()
    print(f"Accepting connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr,inb=b"",outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn,events,data=data)


def service_connection(key,mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data=sock.recv(1024)
        if recv_data:
            data.outb+=recv_data
        else:    
            sel.unregister(sock)
            sel.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} {data.addr}")
            sent=sock.send(data.outb)
            data.outb=data.outb[sent:] 

if len(sys.argv) !=3:
    print(f"Usage: {sys.argv[0]} <host><port>")
    sys.exit(1)

host,port= sys.argv[1],int(sys.argv[2])
lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind((host,port))
lsock.listen()
print(f"Listening on {(host,port)}")
lsock.setblocking(False)
sel.register(lsock,selectors.EVENT_READ,data=None)

try:
    while True:
        events=sel.select(timeout=None)
        for key,mask in events:
            if key.data is None:
                connect_wrapper(key.fileobj)
            else:
                service_connection(key,mask)
except KeyboardInterrupt:
    print(f"Cought keyboard Interrption,exiting...")
finally:
    sel.close()                