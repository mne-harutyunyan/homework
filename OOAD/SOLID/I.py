# SOLID principles
# Interface Segregation Principle

# bad example

from abc import ABC,abstractmethod

class BadCloudProvider(ABC):
    @abstractmethod
    def storeFile(self):
        ...
    @abstractmethod
    def getFile(self):
        ...
    @abstractmethod
    def createServer(self):
        ...
    @abstractmethod
    def getCDNaddress(self):
        ...

class BadAmazon(BadCloudProvider):
    def storeFile(self):
        print("storing file...")
    def getFile(self):
        print("getting file...")
    def createServer(self):
        print("creating server...")
    def getCDNaddress(self):
        print("getting CDN address...")
class BadDropBox(BadCloudProvider):
    def storeFile(self):
        print("storing file...")
    def getFile(self):
        print("getting file...")
    def createServer(self):
        raise Exception("doesn't have ability to create server...")
    def getCDNaddress(self):
        raise Exception("doesn't have ability to get CDN address...")
# obj1 = BadAmazon()
# obj1.createServer()
# obj2 = BadDropBox()
# obj2.createServer()

# good example

class CloudHostingProvider(ABC):
    @abstractmethod
    def createServer(self):
        ...
class CDNprovider(ABC):
    @abstractmethod
    def getCDNaddress(self):
        ...
class CloudStorageProvider(ABC):
    @abstractmethod
    def storeFile(self):
        ...
    @abstractmethod
    def getFile(self):
        ...

class GoodAmazon(CloudHostingProvider,CDNprovider,CloudStorageProvider):
    def createServer(self):
        print("Good Amazon is creating server...")
    def getCDNaddress(self):
        print("Good Amazon is getting CDN address...")
    def storeFile(self):
        print("Good Amazon is storing file...")
    def getFile(self):
        print("Good Amazon is getting file...")

class GoodDropbox(CloudStorageProvider):
    def storeFile(self):
        print("Good Dropbox is storing file...")
    def getFile(self):
        print("Good Dropbox is getting file...")
obj = GoodAmazon()
obj.createServer()
obj2 = GoodDropbox()
obj2.storeFile()