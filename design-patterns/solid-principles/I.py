"""
I stands for Interface Segregation Principle
==> Make fine-grained client-specific interface instead of making generic interfaces

"""

class Machine:

    def print(self, document):
        raise NotImplemented

    def fax(self, document):
        raise NotImplemented

    def scan(self, document):
        raise NotImplemented


"""
Make client-specific interfaces
"""
from abc import ABC, abstractmethod

class PrintMachine(ABC):
    @abstractmethod
    def print(self, document):
        pass

class FaxMachine(ABC):
    def fax(self, document):
        pass

class Scanner(ABC):
    def scan(self, document):
        pass

class PhotoCopier(PrintMachine, FaxMachine):

    def print(self, document):
        pass
    def fax(self, document):
        pass


