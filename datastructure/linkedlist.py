class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

# 1. 특정 원소 참조
# 2. 리스트 순회
# 3. 길이 얻어내기
# 4. 원소 삽입
# 5. 원소 삭제
# 6. 두 리스트 합치기


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if 1 > pos or pos > self.nodeCount:
            raise IndexError

        curr = self.getAt(pos)

        if pos == 1:
            if self.nodeCount == 1:
                self.head = None
                self.tail = None
            else:
                self.head = curr.next
        else:
            prev = self.getAt(pos - 1)
            if pos == self.nodeCount:
                self.tail = prev
                self.tail.next = None
            else:
                prev.next = curr.next

        self.nodeCount -= 1
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
