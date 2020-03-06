

class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        '''是否为空'''
        return self.__head == None

    def length(self):
        '''长度'''
        #cur游标，用来移动遍历节点
        cur = self.__head
        #count 记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next  #cur == None返回
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:  #if cur.next == None then the last data not print
            print(cur.elem,end=" ")
            cur = cur.next

    def add(self,item):
        '''添加节点'''
        node = Node(item)
        node.next = self.__head
        self.__head = node    #新的头部

    def append(self,item):
        '''链表尾部添加节点 尾插发'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self,pos,item):
        '''指定位置添加'''
        if pos < 0:
            self.add(item)
        elif pos > (self.length()-1):
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
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        '''查找节点是否存在'''
        cur = self.__head
        while not cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.append(2)
    ll.append(12)
    ll.append(21)
    ll.append(22)
    ll.append(1)
    ll.travel()
    print(ll)
