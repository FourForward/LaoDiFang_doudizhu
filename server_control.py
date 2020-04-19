"""
服务端
"""
from socket import *
import server_mysql


class ServerControl:
    def __init__(self, addr: str, port: int, password:str):
        self._socket = socket()
        self._socket.bind((addr, port))
        self._socket.listen()
        self._dict_command = {}
        self._database = server_mysql.Database('laodifang_doudizhu',password)

    def main(self):
        self._database.initialize_databese()







if __name__ == '__main__':
    abc = ServerControl('0.0.0.0',12345,'mu7401889')
    abc.main()

