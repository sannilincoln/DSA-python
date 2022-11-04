
class MyList:
    count = 0

    def __init__(self, items,):
        self.items = [items]

    # def count(self):
    #     return len(self.items)

    def printMylist(self):
        for i in self.items:
            print(i)

    def insertEnd(self, e):
        self.items.append(e)
        MyList.count += 1

    def insertAtN(self, n, e):
        movingIndex = MyList.count
        while (movingIndex > n):
            self.items[movingIndex] = self.items[movingIndex - 1]
            movingIndex -= 1

        self.items[n] = e

        MyList.count += 1

    # def removeAtN(self, n):
    #     self.items.remove(n)


arr = MyList([])
arr.insertEnd(1)
arr.insertEnd(1)
arr.insertEnd(1)
arr.insertEnd(1)
arr.insertEnd(1)
arr.insertEnd(1)
arr.insertEnd(1)

arr.insertAtN(2, 56)

arr.printMylist()
print("size  is {}".format(arr.count))
