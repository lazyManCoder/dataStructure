class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLink(object):
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item,end=" ")
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
        rear = self.__head
        if self.is_empty():
            return
        while cur.next != self.__head:
            #先判断是否为头结点
            if cur.item == item:
                if cur == self.__head:
                    #找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next   #在头结点中删除节点
                    rear.next = self.__head
                else:
                    #中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.item == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next



    def search(self,item):
        cur = self.__head
        while not cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    ll = SingleLink()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.remove(20)
    ll.travel()





