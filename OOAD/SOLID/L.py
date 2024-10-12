# SOLID principles
# Liskov Subtitutions Principle

# bad example

class BadDocumentCls:
    def __init__(self,filename) -> None:
        self.__filename = filename
    def open(self):
        print(f"Opening {self.__filename}...")
    def save(self):
        print(f"Saving {self.__filename}...")

class ReadOnlyDocument(BadDocumentCls):
    def __init__(self, filename) -> None:
        super().__init__(filename)
    def save(self):
        raise Exception("Can't save read only document...")

class BadProject:
    def __init__(self, documents : 'BadDocumentCls') -> None:
        self.documents = documents
    def OpenAll(self):
        for document in self.documents:
            document.open()
    def SaveAll(self):
        for document in self.documents:
            document.save()

# doc1 = BadDocumentCls("myfile1")
# doc2 = ReadOnlyDocument("myfile2")

# project = BadProject([doc1, doc2])
# project.OpenAll()  
# project.SaveAll()

# good example
from abc import ABC

class GoodDocumentCls(ABC):
    def __init__(self,filename) -> None:
        self.filename = filename
    def open(self):
        print(f"Opening {self.filename}...")

class WritableDocument(GoodDocumentCls):
    def save(self):
        print(f"Saving {self.filename}...")

class Project:
    def __init__(self, allDocs, writableDocs):
        self.allDocs = allDocs
        self.writableDocs = writableDocs

    def openAll(self):
        for document in self.allDocs:
            document.open()

    def saveAll(self):
        for document in self.writableDocs:
            document.save()

doc1 = WritableDocument("Mydoc1")
doc2 = GoodDocumentCls("Mydoc2") 

project = Project([doc1, doc2], [doc1])
project.openAll()
project.saveAll()
