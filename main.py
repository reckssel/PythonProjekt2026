import socket

def check_port(host, port):
    try:
        whith socket.create_connection((host, port), timeout=5) as sock:
            print(f"Port {port} is open on {host}.")
    except Exception as e:
        print(f"Port {port} is closed on {host}. Error: {e}")