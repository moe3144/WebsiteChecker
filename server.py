import socket

class Server:
    def __init__(self, name, port):
        """Server Initialization
        Accepts Website name and Port# """
        self.name = name
        self.port = port
        self.status = ""
        self.ip = ""

    def is_running(self):
        """Check if the website is reachable"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((self.name, self.port))
            sock.settimeout(None)
            self.ip = sock.getpeername()[0]
            return True
        except socket.error:
            return False

    def __str__(self):
        """Print Server Status"""
        if self.ip:
            return f"{self.name}:{self.port} [{self.ip}] -> {self.status}"
        else:
            return f"{self.name}:{self.port} -> {self.status}"
        