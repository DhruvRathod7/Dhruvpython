from abc import ABC, abstractclassmethod, abstractmethod


class InvalidOperationError(Exception):
    pass


class stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("File is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("File is already close")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(stream):

    def read(self):
        print("Reading data from file")


class NetworkStream(stream):

    def read(self):
        print("Reading data from file")


fs = FileStream()
fs.open()
fs.read()
fs.close()
