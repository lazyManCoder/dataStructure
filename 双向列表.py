class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

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
        # 原头节点的前驱区指向待插入节点
        self.__head.prev = node
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
            cur = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur  #这个链子是一个一个的断开
            node.prev = cur.prev
            cur.prev = node
            cur.next.prev = node



    def remove(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                    break
            else:
                cur = cur.next

    def search(self,item):
        cur = self.__head
        while not cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False



ll = SingleLink(10)
ll.length()
ll.travel()


