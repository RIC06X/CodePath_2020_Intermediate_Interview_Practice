class LinkedNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        
    def show(self):
        current = self.head
        ret = []
        while current is not None:
            ret.append(str(current.val))
            current = current.next
        print('->'.join(ret), self.count)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.count:
            return -1
        if index > self.count // 2:
            current = self.tail
            cnt = self.count - index - 1
            while cnt >= 0:
                current = current.prev
                cnt -= 1
            return current.val
        else:
            current = self.head
            cnt = index
            while cnt >= 0:
                current = current.next
                cnt -= 1
            return current.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        ln = LinkedNode(val)
        ln.next = self.head.next
        ln.prev = self.head
        self.head.next.prev = ln
        self.head.next = ln
        self.count += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        ln = LinkedNode(val)
        ln.next = self.tail
        ln.prev = self.tail.prev
        self.tail.prev.next = ln
        self.tail.prev = ln
        self.count += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.count:
            return
        if index == self.count:
            return self.addAtTail(val)

        ln = LinkedNode(val)
        if index > self.count // 2:
            current = self.tail
            cnt = self.count - index
            while cnt > 0:
                current = current.prev
                cnt -= 1
            ln.prev = current.prev
            ln.next = current
            current.prev.next = ln
            current.prev = ln   
        else:
            current = self.head
            cnt = index
            while cnt > 0:
                current = current.next
                cnt -= 1
            ln.next = current.next
            ln.prev = current
            current.next.prev = ln
            current.next = ln
        self.count += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.count:
            return
        if index > self.count // 2:
            current = self.tail
            cnt = self.count - index - 1
            while cnt > 0:
                current = current.prev
                cnt -= 1
            deleted = current.prev
            current.prev = current.prev.prev
            current.prev.next = current
            deleted.next = deleted.prev = None
        else:
            current = self.head
            cnt = index
            while cnt > 0:
                current = current.next
                cnt -= 1
            deleted = current.next
            current.next = current.next.next
            current.next.prev = current
            deleted.next = deleted.prev = None
        self.count -= 1

作者：haoyuhu
链接：https://leetcode-cn.com/problems/design-linked-list/solution/707-she-ji-lian-biao-by-haoyuhu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。