

from imp import NullImporter


class MyList:

    def __init__(self, items):
        self.items = items
        self.count = len(items)

    def printMylist(self):
        # for i in self.items:
        #     print(i)

        print(self.count)

    def insertEnd(self, e):
        self.items[self.count] = e

    # def insertAtN(self,n,e):
    #     for i in self.items:

    def removeAtN(self, n):
        self.items.reomove(n)


arr = MyList([])

arr.printMylist()
