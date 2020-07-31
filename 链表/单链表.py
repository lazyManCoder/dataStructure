class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLink(object):
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):

        if pos < 0:
            self.add(item)
        if pos > self.length():
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self.__head
        while not cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False





