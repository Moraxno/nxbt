import socket
from multiprocessing import Thread

def serve_loop(conn, addr):
    stop = False
    
    while not stop:
        print(conn, addr)


def listen_loop():
    with socket.socker(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 8123))
        s.listen()

        while True:
            conn, addr = s.accept()
            serve_loop(conn, addr)


def main():
    pass
